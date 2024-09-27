 salary=int(input("Enter salary:"))
age=int(input("Enter age:"))
if(salary>20000 or age<25):
    print("You are Elgible")
    loan=int(input("Loan Amount:"))
    if(loan>50000):
        print("Maximum loan amount is 50000")
    else:
        print("You are elgible for loan")
else:
    print("Not Elgible")
