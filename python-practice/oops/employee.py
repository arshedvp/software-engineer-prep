class Employee:
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