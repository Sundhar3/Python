class dad:
    def phone(self):
        print("Dad's phone")

class mom:
    def sweet(self):
        print("Mom's sweet")

class son(dad,mom):
    def laptop(self):
        print("Son's laptop")

s1=son()
s1.laptop()
s1.phone()
s1.sweet()
