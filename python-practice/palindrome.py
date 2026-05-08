x=input("Enter the string: ").lower()
reverse=""
for char in x:
    reverse = char + reverse
if x == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
