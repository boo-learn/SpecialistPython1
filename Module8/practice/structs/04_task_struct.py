# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один

dict = dictionary_1.copy()
for key, items in dictionary_2.items():
    dict[key] = items
print(dict)
