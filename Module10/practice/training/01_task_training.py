# Напишите программу, вычисляющую площадь всех граней и объем прямоугольного параллелепипеда.

# Важно!
# Оформите решение так, что работа с вашей программой была удобна пользователю.
# Пользователь должен понимать, что его просят ввести и что именно делает программа.

def parr():
    a = float(input("Введите сторону: "))
    b = float(input("Введите еще одну сторону: "))
    c = float(input("Введите еще одну сторону: "))
    sq_parr = 2 * (a * b + b * c + a * c)
    sq_volume = a * b * c
    return sq_parr, sq_volume


sq_square = parr()[0]

sq_volume = parr()[1]

print('Площадь параллелепипеда равна', sq_square, 'Объем параллелепипеда равен', sq_volume)
