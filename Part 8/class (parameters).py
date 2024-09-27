class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno

    def display(self):
        print("Name:",self.name)
        print("Regno:",self.regno)

t1=teacher("Sundhar","03")
t2=teacher("Gowtham","10")

t1.display()
t2.display()
