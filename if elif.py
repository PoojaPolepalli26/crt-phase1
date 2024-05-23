a=int(input("enter the integer:"))
if a%3==0 and a%5==0:
    print("greate")
elif a%3==0 and a%9==0:
    print("good")
elif a%3==0 and a%7==0:
    print("ok")
else:
    print("not ok")
