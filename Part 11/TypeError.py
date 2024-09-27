try:
    a=int(input())
    b=int(input())
    c=input()
    print(c/a)
except ValueError as e:
    print("ValueError",e)
except TypeError as e:
    print("TypeError",e)
