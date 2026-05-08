def reverse(x):
    reversed=""
    for char in x:
        reversed=char+reversed
    return reversed


j=input("Enter the string:")
out=reverse(j)
print("Reversed string: ",out)