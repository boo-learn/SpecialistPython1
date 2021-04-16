# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.
import random

seq = []
digits = "0123456789"

for _ in range(20000):
    seq.append(digits[random.randint(0,9)])

with open("huge_number.txt", "w") as f:
    f.write(''.join(seq))

