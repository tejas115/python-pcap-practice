'''This script automates log parsing for error detection'''
import re

def parse_log(file_path, error_pattern):
    ''' This function parses the log file and extracts lines matching the error pattern '''
    errors = []
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(error_pattern, line):
                errors.append(line.strip())
    return errors

# Usage : errors = parse_log("path/to/logfile.log", r"ERROR|CRITICAL")

print(errors)
print(f"Total errors found: {len(errors)}")