list1=[1, 3, 4, 2, 3, 4, 5, 7, 9, 4, 3]
list2=[]

for i in list1:
    if list1.count(i)==1:
        list2.append(i)
print(list2)