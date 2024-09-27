class a():
    def __init__(self):
        print("Function(1)=A")

    def display(self):
        print("You are in class A")

class b(a):
    def __init__(self):
        super().__init__() #!
        print("Function(2)=B")

    def display(self):
        print("You are in class B")

obj=b()  #call b 
