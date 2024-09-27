class company():
    def __init__(self):
        self.__companyname="Google" #__

    def display(self):
        print(self.__companyname)

c1=company()
c1.display()
print(c1.companyname)

"""
self.companyname = public

self._companyname = protected

self.__companyname = private

"""
