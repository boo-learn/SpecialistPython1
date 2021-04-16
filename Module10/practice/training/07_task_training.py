# Напишите программу генерирующую и записывающую
# в файле произвольное 20000-значное целое число.
import random

with open("data/generate_.txt", "w", encoding='utf-8') as file:
    for x in range(20000):
        rand_int = random.randint(0, 9)
        file.write(str(rand_int))
