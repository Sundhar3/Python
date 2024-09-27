Num1=int(input("Enter Num1:"))
Num2=int(input("Enter Num2:"))
operator=input("add/sub/mul/div:")
if(operator=="add"):
    print(Num1+Num2)
elif(operator=="sub"):
    print(Num1-Num2)
elif(operator=="mul"):
    print(Num1*Num2)
elif(operator=="div"):
    print(Num1/Num2)
else:
    print("Invalid Operator")
