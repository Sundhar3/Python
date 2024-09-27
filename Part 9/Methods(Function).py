class laptop:
    chargertype="B type"

    def __init__(self):
        self.brand=""
        self.price=10000

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

    @classmethod    #Method
    def changechargertype(cls):
        cls.chargertype="C type"
        print("chargertype change  B to C")

    @staticmethod   #Method
    def info():
        print("This is laptop class")

hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechargertype() #cls method
hp.info()

        
