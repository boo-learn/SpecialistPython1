# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]

# TODO: your code here
# Нужно получить словарь:
# {'name': 'Петр', 'surname': 'Первый', 'age': 42, 'rate': 1300}

my_dict = {}
i = 0

for key in keys:
    my_dict[key] = values[i]
    i += 1

for key1, value1 in my_dict.items():
    print(key1, value1)
