x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

while True:
        try:

            j=input("""
    Enter the following keys for the operations mentioned:
                    A for Addition
                    S for Subtraction
                    M for Multiplication
                    D for Division
                    E for Exit
    Enter the key: """).upper()
            
            if j == "E":
                print("Exiting Calculator")
                break
            elif j == "A":
                print(f"The sum of the given numbers is: {x+y}")
            elif j == "S":
                print(f"The difference of the given numbers is: {x-y}")
            elif j == "M":
                print(f"The product of the given numbers is: {x*y}")
            elif j == "D":
                print(f"The quotient of the given numbers is: {x/y}")
            else:
                print("Invalid operation")

        except ZeroDivisionError:
            print("Cannot be divided with zero")

        except ValueError:
            print("Enter valid integers")
                