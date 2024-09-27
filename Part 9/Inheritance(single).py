class dad:
    def phone(self):
        print("Dad's phone")

class son(dad):#(! cls access)
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.laptop()
ram.phone()
