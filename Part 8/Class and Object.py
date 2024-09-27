class trip():
    Role=""
    place=""
    budget=""
    def twodays(self):
        print("Food,viewpoint,waterfalls etc..")
    def oneweek(self):
        print("Beach,party etc..")

Sundhar=trip()
Gowtham=trip()

Sundhar.Role="Founder"
Gowtham.Role="Co-Founder"

Sundhar.place="Bengalur"
Gowtham.place="Goa"

Sundhar.budget=5000
Gowtham.budget=10000

Sundhar.twodays()
Gowtham.oneweek()
