s_Username="Sundhar"
s_Password="123"

u_name=input("Enter Username:")
u_password=input("Enter Password:")

def validation():
    if(s_Username==u_name and s_Password==u_password):
        return True
    else:
        return False

a=validation()
print(a)
