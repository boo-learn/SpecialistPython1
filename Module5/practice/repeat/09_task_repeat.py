# Дан список с названиями фруктов, орехов и ягод.
# Определите, названий начинающихся на какую(какие) букву(буквы) больше всего.
# Известно, что названия могут начинаться как с заглавной, так и с маленькой буквы.
# Примеры
# Дано: [“ананас”, “кокос”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к” больше.
# Дано: [“ананас”, “яблоко”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к”и “а” больше.
def list_char_count(fruit_list):
    list_chars=[]
    for word in fruit_list:
        list_chars.append(word.lower()[0])
    list_counts=[]
    count=0
    for char in list_chars:
        if count<list_chars.count(char):
            count=list_chars.count(char)
    for char in list_chars:
        if count==list_chars.count(char) and char not in list_counts:
            list_counts.append(char)
    return list_counts
print(list_char_count(['ананас', 'кокос', 'Арбуз', 'киви', 'Клюква', 'банан', 'хурма']))
