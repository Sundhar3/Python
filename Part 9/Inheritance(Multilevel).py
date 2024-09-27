class grandpa:
    def phone(self):
        print("Grandpa's phone")

class dad(grandpa): #(!)
    def money(self):
        print("Dad's money")

class son(dad): #(!)
    def laptop(self):
        print("Son's laptop")

aravind=son()
aravind.laptop()
aravind.money()

d1=dad()
d1.phone()
