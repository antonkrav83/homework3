n = int(input("Введите количество школьников N: "))                         
languages=[]
for i in range(n):
    num_lang = int(input(f"Введите количество языков {i+1} школьника: "))
    for j in range(num_lang):
        language = input(f"Введите язык {j+1} школьника {i+1}: ")
        languages.append(language)
lang_all_stud = []
for k in languages:
    if languages.count(k) == n:
        lang_all_stud.append(k)
print("Количество языков которые знают все школьники: ", len(set(lang_all_stud))) 
print("Список языков, которые занают все школьники: ", set(lang_all_stud)) 
print("Количество языков, которые знает хотя бы один школьник: ", len(set(languages)))
print("Список языков, которые знает хотя бы один школьник: ", set(languages)) 

