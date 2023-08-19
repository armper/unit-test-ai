# check_test_errors.py

import xml.etree.ElementTree as ET

def check_test_errors():
    tree = ET.parse('target/surefire-reports/TEST-YourTestClass.xml')
    root = tree.getroot()

    errors = int(root.get('errors'))
    failures = int(root.get('failures'))

    if errors > 0 or failures > 0:
        print("Test errors detected.")
        return True
    else:
        print("No test errors detected.")
        return False

if __name__ == "__main__":
    if check_test_errors():
        exit(1)  # Exit with a non-zero status to indicate errors
