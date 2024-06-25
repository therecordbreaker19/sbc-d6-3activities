 #PALINDROME
def is_palindrome(jar):

    jar = jar.replace(" ", "").lower()

    return jar == jar[::-1]

jeje = input("Enter the Word: ")
if is_palindrome(jeje):
    print(f"'{jeje}' is a palindrome.")
else:
    print(f"'{jeje}' is not a palindrome.")