list=[1, 5, 0, 7, 0, 3, 0]
for i in range(len(list)):
    if list[i]!=0:
        print(list[i], end=' ')
for i in range(list.count(0)):
        print(0,end=' ')