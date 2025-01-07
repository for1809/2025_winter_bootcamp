# 5. Toggle Case of Each Character in a String
# Write a function `toggle_case(text)` that takes a string `text` and returns a new string with each uppercase letter converted to lowercase and each lowercase letter converted to uppercase.

# ### Requirements
# *   Use a `for` loop to iterate through each character in the string.
# *   If a character is uppercase, convert it to lowercase.
# *   If a character is lowercase, convert it to uppercase.
# *   Leave non-alphabetic characters unchanged.
# *   Ensure that the function produces the expected output for the given test cases.



def toggle_case(text):
    # Write your code here
    return text.swapcase()