a = int(input("Введите количество стран: "))                         
countries={}                                                         
for i in range(a):                                                    
    country = input("Введите название страны и ее города через пробел: ")    
    list_country = country.split()                                           
    for key in list_country:                                                 
        countries[key] = list_country[0]                                     
    del countries[list_country[0]]                                           
b = int(input("Введите количество городов: "))
for j in range(b):                                                           
    city = input(f"Введите название {j+1} города: ")                                
    print("Страна: ", countries.get(city)) 
