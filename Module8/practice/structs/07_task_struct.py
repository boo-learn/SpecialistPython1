# Доработайте предыдущую программу так, чтобы каждый сгенерированный сотрудник
# был уникальным(не должны повторяться комбинации Имя + Фамилия).
import random

symbols = 'абвгдейжзийклмнопрстуфхцчшщъыьэюя'
positions = ('директор','менеджер','программист','уборщик','охранник')
test_staff = {}

n = input("n: ")
i = 1
while i <= n:
    given_name = ''.join([symbols[random.randint(0,32)] for _ in range(random.randint(3,10))]).title()
    last_name = ''.join([symbols[random.randint(0,32)] for _ in range(random.randint(5,10))]).title()
    age = random.randint(18,65)
    position = positions[random.randint(0,4)]
    salary = random.randint(10, 100) * 1000

    name_key = '_'.join((last_name, given_name))
    if not test_staff.get(name_key):
        test_staff[name_key] = {"GivenName": given_name, "LastName" : last_name, "Age": age, "Position": position, "Salary": salary}
        i += 1

print(test_staff)
