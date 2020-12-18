# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один
l1 = tuple(dictionary_1.items())
l2 = tuple(dictionary_2.items())
dicts = dict(l1 + l2)
print(dicts)
