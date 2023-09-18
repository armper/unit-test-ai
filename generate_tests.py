import openai
import os
import requests
import json


def extract_package_declaration(class_code):
    """
    Extract the package declaration from the given Java class code.
    """
    for line in class_code.split('\n'):
        line = line.strip()
        if line.startswith("package "):
            return line


def call_openai_to_generate_test(class_code, existing_test_code=None):

    # Set the API key
    openai.api_key = os.environ['OPENAI_API_KEY']
    print(f"Using API Key: {openai.api_key}")

    # Create a message for ChatGPT based on whether an existing test code is provided
    if existing_test_code:
        user_message = f'Update the following unit test for the Java class: {class_code}\nExisting Test:\n{existing_test_code}'
    else:
        user_message = f'Generate a unit test for the following Java class: {class_code}'

    messages = [
        {
            "role": "system",
            "content": "You will be provided with a piece of Java code, and your task is to return a complete unit test for that code. Use only Junit 5. Return nothing but the code with no additional text."
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    # Call ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-4", messages=messages,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    # Extract the generated test code from the response
    test_code = response.choices[0].message.content.strip()

    # Extract the package declaration from the class code
    package_declaration = extract_package_declaration(class_code)

    # Check if the generated test code has a package declaration
    if package_declaration and "package " not in test_code:
        test_code = package_declaration + "\n\n" + test_code

    if test_code:
        return test_code
    else:
        print("Failed to generate test code.")
        return None


def generate_tests_for_class(class_path):
    # Extract the class name from the file path
    class_name = os.path.basename(class_path).replace('.java', '')

    # Determine the base path for the test file by replacing "src/main" with "src/test"
    test_base_path = class_path.replace('src/main', 'src/test')

    # Read the class code
    with open(class_path, 'r') as file:
        class_code = file.read()

    # Check if the test file already exists
    existing_test_path = test_base_path.replace(
        f'{class_name}.java', f'{class_name}Test.java')

    existing_test_code = None
    if os.path.exists(existing_test_path):
        with open(existing_test_path, 'r') as file:
            existing_test_code = file.read()

    # Call OpenAI to generate or update the test code
    test_code = call_openai_to_generate_test(class_code, existing_test_code)
    if test_code is None:
        print(f"Failed to generate test for {class_path}")
        return None

    # Write the test code to the file
    with open(existing_test_path if existing_test_code else test_base_path.replace(f'{class_name}.java', f'{class_name}Test.java'), 'w') as file:
        file.write(test_code)

    # Return the path for use in the Jenkins pipeline
    return existing_test_path if existing_test_code else test_base_path.replace(f'{class_name}.java', f'{class_name}Test.java')


# Read the changed files from the file generated earlier in the Jenkins pipeline
with open('changed_files.txt', 'r') as file:
    changed_files = file.readlines()

# Iterate through the changed files and generate tests for each class
for class_path in changed_files:
    class_path = class_path.strip()  # Remove newline characters

    # Check if the file is a Java class and not from the "src/test" directory
    if class_path.endswith('.java') and "src/test" not in class_path:
        test_file_path = generate_tests_for_class(class_path)
        if test_file_path:
            # Write the path to a file for use in the Jenkins pipeline
            with open('generated_test_path.txt', 'a') as file:
                file.write(test_file_path + '\n')
