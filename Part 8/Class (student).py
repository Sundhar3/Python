class student:
    def __init__(self):
        self.name=""
        self.regno=""
    def display(self):
        print("Name:",self.name)
        print("Reg.no:",self.regno)

s1=student()
s2=student()

s1.name="Sundhar"
s1.regno="02"

s2.name="Suresh"
s2.regno="01"

s1.display()
s2.display()
