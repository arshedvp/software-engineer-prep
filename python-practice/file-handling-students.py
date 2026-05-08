username = input("Enter the user name: ")
age = input("Enter the age: ")

with open("student.txt", "w") as file:
    file.write((f"User name is : {username}\nage is {age}"))