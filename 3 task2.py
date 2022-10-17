my_list = [a + b for a in "ab" for b in "bcd" ]
print(my_list)
list1 = my_list[::2]
print(list1)
list2 = [str(x) + "a" for x in range(1, 5)]
print(list2)
list2.remove("2a")
print(list2)
import copy
list3 = copy.deepcopy(list2) 
list3.append("2a")
print("Исходный список: ", list2)
print("С добавлением список: ", list3)



   
     

