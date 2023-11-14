def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()

    # Compare the original string with its reverse
    return s == s[::-1]


# Example usage calling the function
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")