a=int(input("enter the a marks:"))
b=int(input("enter the b marks:"))
c=int(input("enter the c marks:"))
if a>80 and b>80 and c>80:
    print("A+")
elif a>60 and b>60 and c>60 and a<80 and b<80 and c<80:
    print("B+")
else:
    print("pass")
