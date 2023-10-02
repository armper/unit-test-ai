import os
import openai

def check_test_errors(error_file):
    """Check if there are any test errors by reading the error file."""
    with open(error_file, 'r') as file:
        content = file.read().strip()
        return bool(content)

def extract_errors_from_file(error_file):
    """Extract the error messages from the error file."""
    with open(error_file, 'r') as file:
        return file.read()

def fix_errors(test_path, current_unit_test_code, test_errors):
    """Attempt to fix the test errors using the OpenAI API."""
    user_message = f'Fix the following errors in this Java unit test code:\n{current_unit_test_code}\nErrors:\n{test_errors}'

    messages = [
        {
            "role": "system",
            "content": "You are provided with a piece of Java unit test code with errors. Your task is to return the corrected code. Use only Junit 5. Return nothing but the code with no additional text."
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if response['choices'] and response['choices'][0]['message']['role'] == 'assistant':
        fixed_test_code = response['choices'][0]['message']['content']

        # Overwriting the original test file with the corrected code using the full path
        with open(test_path, 'w') as file:
            file.write(fixed_test_code)
    else:
        print('Error: Failed to get corrected code from OpenAI.')

if __name__ == "__main__":
    openai.api_key = os.environ['OPENAI_API_KEY']

    error_file = 'testErrors.txt'
    error_detected = False

    # Ensure the fixed_tests directory exists
    fixed_tests_dir = 'fixed_tests'
    if not os.path.exists(fixed_tests_dir):
        os.makedirs(fixed_tests_dir)

    with open('generated_test_path.txt', 'r') as file:
        generated_tests = [os.path.abspath(line.strip()) for line in file.readlines()]

    print("Current Working Directory:", os.getcwd())

    if check_test_errors(error_file):
        print("Test errors detected. Attempting to fix...")

        for test_path in generated_tests:
            test_name = os.path.basename(test_path).replace('.java', '')
            print(f"Checking {test_name}...")

            # Fetching the current unit test code
            with open(test_path, 'r') as code_file:
                current_unit_test_code = code_file.read()

            # Extracting test errors from the error file
            test_errors = extract_errors_from_file(error_file)

            fix_errors(test_path, current_unit_test_code, test_errors)
            error_detected = True

    if not error_detected:
        print("No test errors detected.")
