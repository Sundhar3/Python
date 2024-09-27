
def add(a,b,c):
    print(a+b)   

#add(10,20) =Error

def add(a,b,c=0):
    print(a+b+c)

add(10,20)
add(10,20,30)
