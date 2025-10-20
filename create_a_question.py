import os
import json
import shutil
import re

# Constants
JSON_FILE = 'new_files.json'
SOLUTION_TEMPLATE = 'solutions/question_template.py'
TEST_TEMPLATE = 'tests/test_blank.py'
SOLUTION_DIR = 'solutions'
TEST_DIR = 'tests'

def sanitize_filename(name):
    # Replace hyphens with underscores, remove invalid characters
    name = name.replace('-', '_')
    name = re.sub(r'\W+', '', name)  # Remove non-alphanumeric/underscore
    return name

def extract_filename_from_url(url):
    match = re.search(r'problems/([^/]+)/description', url)
    if match:
        return sanitize_filename(match.group(1))
    return None

def main():
    if not os.path.exists(JSON_FILE):
        print(f"❌ JSON file '{JSON_FILE}' not found.")
        return

    with open(JSON_FILE, 'r') as f:
        entries = json.load(f)

    for entry in entries:
        url = entry.get('url')
        if not url:
            continue

        filename = extract_filename_from_url(url)
        if not filename:
            print(f"⚠️ Could not extract filename from URL: {url}")
            continue

        solution_path = os.path.join(SOLUTION_DIR, f"{filename}.py")
        test_path = os.path.join(TEST_DIR, f"test_{filename}.py")

        if os.path.exists(solution_path) and os.path.exists(test_path):
            print(f"✅ Files already exist for '{filename}', skipping...")
            continue

        # Copy and fill solution template
        if not os.path.exists(solution_path):
            shutil.copyfile(SOLUTION_TEMPLATE, solution_path)
            with open(solution_path, 'r+') as f:
                content = f.read()
                # Define the pattern to replace
                pattern = re.compile(
                    r"################################################\n"
                    r"#\s*\n"
                    r"# Leetcode: .*\n"
                    r"# URL: .*\n"
                    r"# Difficulty: .*\n"
                    r"#\s*\n"
                    r"################################################",
                    re.MULTILINE
                )

                # Create the replacement header
                replacement = (
                    "################################################\n"
                    f"# \n"
                    f"# Leetcode: {entry.get('leetcode_number', 'N/A')} \n"
                    f"# URL: {entry.get('url', 'N/A')} \n"
                    f"# Difficulty: {entry.get('diffculty', 'N/A')} \n"
                    f"# \n"
                    "################################################"
                )

                # Replace the pattern in the content
                updated_content = re.sub(pattern, replacement, content)
                f.seek(0)
                f.write(updated_content)
                f.truncate()
            print(f"📝 Created solution file: {solution_path}")

        # Copy test template
        if not os.path.exists(test_path):
            shutil.copyfile(TEST_TEMPLATE, test_path)
            print(f"🧪 Created test file: {test_path}")

if __name__ == "__main__":
    main()
