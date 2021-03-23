# Дан список с названиями фруктов, орехов и ягод.
# Определите, названий начинающихся на какую(какие) букву(буквы) больше всего.
# Известно, что названия могут начинаться как с заглавной, так и с маленькой буквы.
# Примеры
# Дано: [“ананас”, “кокос”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к” больше.
# Дано: [“ананас”, “яблоко”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к”и “а” больше.

from collections import Counter

# fruits = ["ананас", "кокос", "Арбуз", "киви", "Клюква", "банан", "хурма"]
fruits = ["ананас", "яблоко", "Арбуз", "киви", "Клюква", "банан", "хурма"]
letters = []

for fruit in fruits:
    letter = fruit[0].lower()
    letters.append(letter)

letter_cnt = Counter(letters)

max_letter = max(letter_cnt, key=letter_cnt.get)

# print(letter_cnt)

highest = max(letter_cnt.values())
res = [k for k, v in letter_cnt.items() if v == highest]

# print(res)

for el in res:
    print(f"фруктов на букву '{el}' больше")


