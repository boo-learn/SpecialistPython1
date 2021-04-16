# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один
for key, value in dictionary_2.items():
    s = (key,value)
    dictionary_1.update([s])
print(dictionary_1)
