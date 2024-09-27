class cricket:
    overs="3overs"

    def __init__(self,fast,medium,spin):
        self.fast=fast
        self.medium=medium
        self.spin=spin

    def total(self):
        print("fastblower:",self.fast)
        print("Mediumfast:",self.medium)
        print("Spinner:",self.spin)
        print("Overper blower:",self.overs)

cricket.overs="4overs"

csk=cricket("pathirana","Dude","Jaddu")
csk.total()
