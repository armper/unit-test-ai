# analyze_changes.py

def analyze_file_content(file_name):
    # Example function to analyze the content of a file
    with open(file_name, 'r') as file:
        content = file.read()
        # Perform analysis on the content, e.g., checking coding standards, patterns, etc.
        print(f"Content of {file_name}: {content[:100]}...")  # Print the first 100 characters

def analyze_file_type(file_name):
    # Example function to analyze the file type based on the extension
    file_extension = file_name.split('.')[-1]
    print(f"File extension: {file_extension}")
    return file_extension

with open('changed_files.txt', 'r') as file:
    changed_files = file.readlines()

for file_name in changed_files:
    file_name = file_name.strip()  # Remove newline characters
    print(f"Analyzing file: {file_name}")

    file_extension = analyze_file_type(file_name)

    # Perform specific analysis based on file type
    if file_extension in ['java', 'py', 'js']:
        analyze_file_content(file_name)
    else:
        print(f"Skipping analysis for unsupported file type: {file_extension}")
