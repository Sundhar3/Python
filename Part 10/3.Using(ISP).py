class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,role):
        super().__init__(name,salary)
        self.role=role

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Role:",self.role)

m1=manager("Sundhar","20000","Junior react developer")
m1.display()

        
