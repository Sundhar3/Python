a=[]
sum=0
avg=0
for i in range(5):
    num=int(input("Enter num"+str(i+1)))
    a.append(num)
    sum=sum+num
    avg=sum/5
    print(a)
    print("sum:",sum)
    print("Avg:",avg)
