class fruit:
    def __init__(self,color):
        self.color=color

    def display(self):
        print("color:",self.color)

apple=fruit("red")
apple.display()
