Score=int(input("Enter Score:"))
if(Score<35):
    print("Poor Student")
elif(Score>35 and Score<75):
    print("Average Student")
elif(Score>75 and Score<100):
    print("Good Student")
else:
    print("Invalid Score")
