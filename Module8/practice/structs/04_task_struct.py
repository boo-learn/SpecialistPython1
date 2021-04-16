# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один

def merge_two_dicts(dictionary_1, dictionary_2):
    z = dictionary_1.copy()
    z.update(dictionary_2)
    return z

z = merge_two_dicts(dictionary_1, dictionary_2)

print(z)
