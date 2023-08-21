import os
import requests
import json


def call_openai_to_generate_test(class_code):
    # Check if we're in fake testing mode
    if os.environ.get('FAKE_TESTING_MODE') == 'True':
        # Return a basic boilerplate JUnit test that always succeeds
        return f'''
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class FakeTest {{
    @Test
    public void testAlwaysPasses() {{
        assertTrue(true);
    }}
}}
'''
    # Assuming the API key is set as an environment variable
    api_key = os.environ['OPENAI_API_KEY']
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        'prompt': f'Generate a unit test for the following Java class: {class_code}',
    }
    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)
    if response.status_code == 200:
        return json.loads(response.text)['choices'][0]['text']
    else:
        print(f'Error: {response.text}')
        return None


def generate_tests_for_class(class_path):

    # Extract the class name from the file path
    class_name = os.path.basename(class_path).replace('.java', '')

    # Determine the base path for the test file by replacing "src/main" with "src/test"
    test_base_path = class_path.replace('src/main', 'src/test')

    # Read the class code
    with open(class_path, 'r') as file:
        class_code = file.read()

    # Call OpenAI to generate the test code
    test_code = call_openai_to_generate_test(class_code)
    if test_code is None:
        print(f"Failed to generate test for {class_path}")
        return None

    # Check if the test file already exists
    existing_test_path = test_base_path.replace(
        f'{class_name}.java', f'{class_name}Test.java')
    if os.path.exists(existing_test_path):
        test_file_path = existing_test_path
    else:
        # If not, create a new test file with the appropriate name and path
        test_file_path = test_base_path.replace(
            f'{class_name}.java', f'{class_name}test.java')

    # Write the test code to the file
    with open(test_file_path, 'w') as file:
        file.write(test_code)

    # Return the path for use in the Jenkins pipeline
    return test_file_path


# Read the changed files from the file generated earlier in the Jenkins pipeline
with open('changed_files.txt', 'r') as file:
    changed_files = file.readlines()

# Iterate through the changed files and generate tests for each class
for class_path in changed_files:
    class_path = class_path.strip()  # Remove newline characters
    if class_path.endswith('.java'):  # Check if the file is a Java class
        test_file_path = generate_tests_for_class(class_path)
        if test_file_path:
            # Write the path to a file for use in the Jenkins pipeline
            with open('generated_test_path.txt', 'a') as file:
                file.write(test_file_path + '\n')
