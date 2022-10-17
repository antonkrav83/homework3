import numbers
import re
my_str = input("Введите текст: ")
new_str = re.sub(r'[^\w\s]',' ', my_str)
numbers = new_str.split()
print(len(numbers))  

