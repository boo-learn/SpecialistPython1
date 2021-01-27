# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один

for el in dictionary_2:    # Наверное не совсем корректно (???)
    dictionary_1[el] = dictionary_2[el]       

print(dictionary_1)
