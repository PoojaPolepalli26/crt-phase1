list=[3,5,"hello",1.23,7]
list.append(35)
print(list)
list.insert(3,56)
print(list)
print(list[0])
print(list[2])
for i in range(0,len(list)):
    print(i)
for i in list:
    print(list)
print (list[4])
print (list[1:3])
print (list[:5])
print (list[-1])
list[2]="say"
print(list)
