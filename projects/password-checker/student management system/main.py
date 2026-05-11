from sms import Student

student_list=[]
while True:
    x=int(input("""
1. Add Student
2. View Students
3. Student Count
4.search
5. Exit
Enter your selection: 
          """))
    
    if x ==1:
        name=input("Enter the name: ")
        while True:
            try:        
                age=int(input("Enter the age: "))
                break
            except ValueError:
                print("Please enter valid integer")


       

        course=input("Enter the course: ")

        student=Student(name,age,course)
        student_list.append(student)
        with open("students.txt", "a") as file:
            file.write(f"{name},{age},{course}\n")

    elif x ==2:
        for index, each in enumerate(student_list, start=1):
            print(f"\nStudent {index}")
            each.display()

    elif x ==3:
        print(f"Total count of students: {len(student_list)}")

    elif x == 4:
        search_name=input("Enter student name to search: ")
        found = False
        for each in student_list:
            if each.name.lower()==search_name.lower():
                each.display()

                found = True
        if found== False:
            print("not found")
            
        
    elif x ==5:
        print("Exiting")
        break

    else:
        print("Invalid Operation")

        

        
    



    
    
