import os
import xml.etree.ElementTree as ET
import openai


def check_test_errors(xml_file):
    print("check test errors method")

    tree = ET.parse(xml_file)
    root = tree.getroot()
    print(ET.tostring(root, encoding='utf8').decode('utf8'))

    errors = int(root.attrib['errors'])
    failures = int(root.attrib['failures'])

    print(f"For {xml_file} -> Errors: {errors}, Failures: {failures}")

    return errors > 0 or failures > 0


def extract_errors_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    error_messages = []

    for testcase in root.findall('testcase'):
        for error in testcase.findall('error'):
            error_messages.append(error.get('message'))

    return '\n'.join(error_messages)


def fix_errors(test_path, current_unit_test_code, test_errors):

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
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if response['choices'] and response['choices'][0]['message']['role'] == 'assistant':
        fixed_test_code = response['choices'][0]['message']['content']

        print(test_path)

        # Overwriting the original test file with the corrected code using the full path
        with open(test_path, 'w') as file:
            file.write(fixed_test_code)
    else:
        print('Error: Failed to get corrected code from OpenAI.')


if __name__ == "__main__":
    openai.api_key = os.environ['OPENAI_API_KEY']

    test_reports_dir = 'target/surefire-reports/'
    error_detected = False

    # Ensure the fixed_tests directory exists
    fixed_tests_dir = 'fixed_tests'
    if not os.path.exists(fixed_tests_dir):
        os.makedirs(fixed_tests_dir)

    with open('generated_test_path.txt', 'r') as file:
        generated_tests = [os.path.abspath(
            line.strip()) for line in file.readlines()]

    print("Current Working Directory:", os.getcwd())

    for test_path in generated_tests:
        test_name = os.path.basename(test_path).replace('.java', '')
        print(f"Checking {test_name}...")

        xml_file = f'TEST-{test_name}.xml'
        full_path = os.path.join(test_reports_dir, xml_file)

        print(f"Full path: {full_path}")
        print(f"Does the file exist? {os.path.exists(full_path)}")

        absolute_path = os.path.abspath(full_path)
        print(f"Absolute path: {absolute_path}")
        print(
            f"Does the file exist (absolute path)? {os.path.exists(absolute_path)}")

        if os.path.exists(full_path) and check_test_errors(full_path):
            print(f"Test errors detected in {xml_file}. Attempting to fix...")

            # Fetching the current unit test code
            with open(test_path, 'r') as code_file:
                current_unit_test_code = code_file.read()

            # Extracting test errors from XML report
            test_errors = extract_errors_from_xml(full_path)

            fix_errors(test_path, current_unit_test_code, test_errors)
            error_detected = True

    if not error_detected:
        print("No test errors detected.")
