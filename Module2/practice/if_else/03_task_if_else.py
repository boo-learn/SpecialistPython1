# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.
a = int(input("Please input first side of a triangle: "))
b = int(input("Please input second side of the triangle: "))
c = int(input("Please input third side of the triangle: "))

if a==b or b==c or a==c:
    print("YES")
else:
    print ("NO")
