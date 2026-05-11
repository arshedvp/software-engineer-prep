class employee:
    def __init__(self,name,company,role):
        self.name=name
        self.company=company
        self.role=role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Role: {self.role}")  

    def greet(self):
        print(f"Hello, I am {self.name}")


e1=employee("Arshed","Unisys","ASE")

e1.display()
e1.greet()