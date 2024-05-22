# APPROACH 1
def generate_combinations(word):
    def combinations(current, start, word, all_combinations):
        if current:
            all_combinations.append(''.join(current))
        for i in range(start, len(word)):
            combinations(current + [word[i]], i + 1, word, all_combinations)

    all_combinations = []
    combinations([], 0, word, all_combinations)
    return all_combinations

def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome_length(combinations):
    max_length = 0
    for comb in combinations:
        if is_palindrome(comb):
            max_length = max(max_length, len(comb))
    return max_length

# Read input
n = int(input())
string = input().strip()

# Generate combinations
all_combinations = generate_combinations(string)
# Find the length of the longest palindromic substring
max_length = longest_palindrome_length(all_combinations)
# Print the result
print(max_length)

# APPROACH 2
def longest_palindromic_substring_length(s):
    n = len(s)
    if n == 0:
        return 0
    
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of the palindrome

    max_length = 1
    for i in range(n):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)
        max_length = max(max_length, len1, len2)

    return max_length

# Read input
n = int(input())
string = input().strip()

# Find and print the length of the longest palindromic substring
print(longest_palindromic_substring_length(string))




