class laptop:
    def __init__(self): #constractor (Inbulid function in py)
        self.price=0
        self.ram=""
        self.processor=""

    def display(self):
        print("Price:",self.price)
        print("Ram:",self.ram)
        print("Processor:",self.processor)

hp=laptop()
dell=laptop()

hp.price=40000
hp.ram="8gb"
hp.processor="AMD"

dell.price=60000
dell.ram="16gb"
dell.processor="i7"

hp.display()
dell.display()
