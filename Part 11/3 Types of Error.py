try:
    a=int(input())
    b=int(input())
    c=input()
    print(d)##
except ValueError as e:
    print("ValueError",e)
except TypeError as e:
    print("TypeError",e)
except Exception as e:
    print("Something Wrong",e)
finally:            #Automatically work with or without Error
    print("Done")
