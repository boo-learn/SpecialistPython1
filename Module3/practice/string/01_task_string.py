# Для регистрации на сайте, пользователи часто вводят Имя и Фамилию с маленькой буквы.
# Напишите мини-программу, которая будет запрашивать у пользователя имя и фамилию
# и заменять первые буквы буквами в верхнем регистре.
# Измененные данные(имя и фамилию) вывести на экран.

name = input("Имя: ")
surname = input("Фамилия: ")

name_rp = name[0].upper()
name = name.replace(name[0], name_rp)

surname_rp = surname[0].upper()
surname = surname.replace(surname[0], surname_rp)

print(name, surname)
