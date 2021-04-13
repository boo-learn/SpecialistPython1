# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
tup_1 = (1, 2, 3, 4)
tup_2 = (2, 3, 4)
tup_3 = (3, 3, 5, 4)

repeat = 0

for el_1 in tup_1:
    for el_2 in tup_2:
        if el_1 == el_2:
            for el_3 in tup_3:
                if el_2 == el_3:
                    repeat += 1
                    break
print(repeat)
