# Дан список с названиями фруктов, орехов и ягод.
# Определите, названий начинающихся на какую(какие) букву(буквы) больше всего.
# Известно, что названия могут начинаться как с заглавной, так и с маленькой буквы.
# Примеры
# Дано: ["ананас", "кокос", "Арбуз", "киви", "Клюква", "банан", "хурма"]
# Результат: фруктов на букву "к" больше.
# Дано: ["ананас", "яблоко", "Арбуз", "киви", "Клюква", "банан", "хурма"]
# Результат: фруктов на букву "к"и "а" больше.

def max_count_of_first_char(fruit_list):
    fruit_first_char = []
    for fruit in fruit_list:
        fruit_first_char.append(fruit.lower()[0])
    res_list = []
    count = 0
    for char in fruit_first_char:
        if fruit_first_char.count(char) > count:
            count = fruit_first_char.count(char)
    for char in fruit_first_char:
        if fruit_first_char.count(char) == count and char not in res_list:
            res_list.append(char)
    return res_list


fruits = ["ананас", "яблоко", "Арбуз", "киви", "Клюква", "банан", "хурма"]
print(max_count_of_first_char(fruits))
