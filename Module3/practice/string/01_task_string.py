# Для регистрации на сайте, пользователи часто вводят Имя и Фамилию с маленькой буквы.
# Напишите мини-программу, которая будет запрашивать у пользователя имя и фамилию
# и заменять первые буквы буквами в верхнем регистре.
# Измененные данные(имя и фамилию) вывести на экран.

name = input("Имя: ")
surname = input("Фамилия: ")

new_name = name.capitalize()
new_surname = surname.capitalize()

print(new_name, new_surname)
