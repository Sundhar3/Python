tam=int(input("Tam:"))
eng=int(input("Eng:"))
mat=int(input("Mat:"))
sci=int(input("Sci:"))
ss=int(input("SS:"))
Total=(tam+eng+mat+sci+ss)/5
print("Avg:",Total)
if(Total<50):
    print("Additional class is required")
else:
    print("You are Good")
