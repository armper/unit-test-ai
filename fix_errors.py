import os
import xml.etree.ElementTree as ET
import requests
import json


def check_test_errors(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    errors = int(root.get('errors'))
    failures = int(root.get('failures'))

    return errors > 0 or failures > 0


def fix_errors():
    # Check if we're in fake testing mode
    if os.environ.get('FAKE_TESTING_MODE') == 'True':
        print("In FAKE_TESTING_MODE. Skipping call to OpenAI.")
        return

    api_key = 'YOUR_API_KEY'
    current_unit_test_code = 'YOUR_CURRENT_UNIT_TEST_CODE'
    test_errors = 'YOUR_TEST_ERRORS'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    data = {
        'prompt': 'Fix the following errors in this Java unit test code...',
        'code': current_unit_test_code,
        'errors': test_errors,
    }

    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)

    if response.status_code == 200:
        fixed_test_code = json.loads(response.text)['choices'][0]['text']
        with open('path/to/new_unit_test_file.java', 'w') as file:
            file.write(fixed_test_code)
    else:
        print(f'Error: {response.text}')


if __name__ == "__main__":
    test_reports_dir = 'target/surefire-reports/'
    error_detected = False

    # Read the paths of the newly generated or updated unit tests
    with open('generated_test_path.txt', 'r') as file:
        generated_tests = file.readlines()

    for test_path in generated_tests:
        test_name = os.path.basename(test_path).replace('.java', '')
        xml_file = f'TEST-{test_name}.xml'
        full_path = os.path.join(test_reports_dir, xml_file)

        if os.path.exists(full_path) and check_test_errors(full_path):
            print(f"Test errors detected in {xml_file}. Attempting to fix...")
            fix_errors()
            error_detected = True

    if not error_detected:
        print("No test errors detected.")
