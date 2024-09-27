class phone:
    def __init__(self,brand,price,chargertype):
        self.brand=brand
        self.price=price
        self.chargertype=chargertype

    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargertype:",self.chargertype)

samsang=phone("samsang","12000","B-Type")
samsang.display()

redmi=phone("Redmi","15000","C-type")
redmi.display()

vivo=phone("Vivo","18000","c-type")
vivo.display()
