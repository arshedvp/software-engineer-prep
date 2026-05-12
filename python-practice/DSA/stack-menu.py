stack =[]

while True:
    try:
        x=int(input("""
1.ADD
2.REMOVE
3.DISPLAY
4.EXIT
Enter your selection:
"""))
    except ValueError:
        print("Enter proper input")

    
    if x==1:
        try:
            j=int(input("Enter the number"))
            stack.append(j)
        except ValueError:
            print("Enter integer")

    if x==2:
        print(stack.pop())

    if x==3:
        print(stack)

    if x==4:
        print("Exiting")
        break