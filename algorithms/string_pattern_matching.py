'''String Pattern matching'''
# You are given two strings: pattern and source.
# The first string pattern contains only the symbols 0 and 1,
# and the second string source contains only lowercase English letters.

# Your task is to calculate the number of substrings of source that match pattern. 

# We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
# – The pattern and substring are equal in length.
# – Where there is a 0 in the pattern, there is a vowel in the substring. 
# – Where there is a 1 in the pattern, there is a consonant in the substring. 

# Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.
# Guaranteed constraints:
# 1 ≤ source.length ≤ 103
# 1 ≤ pattern.length ≤ 103

# vowels = ['a', 'e', 'i', 'o', 'u', 'y']
VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}  # ✅ Constant in UPPER_CASE

def check_for_pattern(search_pattern, search_source, start_index):
    '''Check if substring matches pattern'''
    for pos, pattern_char in enumerate(search_pattern):  # Different names
        source_char = search_source[start_index + pos]
        if pattern_char == '0' and source_char not in VOWELS:
            return False
        if pattern_char == '1' and source_char in VOWELS:  # 'if' not 'elif'
            return False
    return True


pattern = input('Enter the string pattern to search in the form of 0 or 1: ')
source = input('Enter the source string containing only lowercase letters: ')

# This is a VARIABLE (changes value), not a constant
matching_count = 0 # pylint: disable=invalid-name

for i in range(len(source) - len(pattern) + 1):
    if check_for_pattern(pattern, source, i):
        matching_count += 1
        # Extract substring from position i with length of pattern
        substring = source[i:i+len(pattern)]  # ✅ String slicing
        print(f"Found matching substring: {substring}")

print(f"Total matching substrings found: {matching_count}")
