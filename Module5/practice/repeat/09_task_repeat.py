# Дан список с названиями фруктов, орехов и ягод.
# Определите, названий начинающихся на какую(какие) букву(буквы) больше всего.
# Известно, что названия могут начинаться как с заглавной, так и с маленькой буквы.
# Примеры
# Дано: [“ананас”, “кокос”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к” больше.
# Дано: [“ананас”, “яблоко”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к”и “а” больше.

fruits= ["ананас", "Баклажан", "Арбуз", "киви", "Клюква", "банан", "хурма"]

first_letters_tup=tuple(map(lambda el: el[0].lower(),fruits))
# first_letters_set=set(map(lambda el: el[0].lower(),fruits))
first_letters_set=set(first_letters_tup)

# Вариант 1 отбора
first_letters_dict={}
for el in first_letters_set:
    first_letters_dict[el]=first_letters_tup.count(el)

# Вариант 2 отбора
first_letters_dict1={el:first_letters_tup.count(el) for el in first_letters_set}

max_count=max(first_letters_dict.values())

# Вариант 1 вывода
max_list=[]
for i in first_letters_dict.items():
    if i[1]==max_count:
        max_list.append(i)
print(f"Буквы, встречающиеся чаще всего без учета регистра {max_list}")

# Вариант 2 вывода
max_list1=list(filter(lambda i:i[1]==max_count,first_letters_dict1.items()))
print(f"Буквы, встречающиеся чаще всего без учета регистра {max_list1}")
