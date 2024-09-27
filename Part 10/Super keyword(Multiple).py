class a():
    def __init__(self):
        print("Function(1)=A")

    def display(self):
        print("You are class A")

class b(a):
    def __init__(self):
        super().__init__() #Function init(a)
        print("Function(2)=B")

    def display(self):
        print("You are in class B")

class c(b,a):
    def __init__(self):
        super().__init__() #Function init(b is first)
        print("Function(3)=C")

    def display():
        print("You are in class C")

obj=c() #!
