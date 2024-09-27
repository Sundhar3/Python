class dad(): #base or parent class
    def money(self):
        print("Dad's money")

class son1(dad):
    pass

class son2(dad):  #child class
    pass

class son3(dad):
    pass


s1=son2()
s1.money()
