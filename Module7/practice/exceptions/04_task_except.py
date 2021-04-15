# Даны два уравнения прямых вида у=kx+b и виде строки. Проверить, пересекаются ли данные прямые?
# Примеры уравнений: "y = 2x + 4"  "y = -12x -12"

# Проверьте входные данные на корректность
import re

pattern = re.compile('y = [-]{0,1}[0-9]{0,}x [+]{0,1}[ ]{0,1}[-]{0,1}[0-9]{0,}')

equation = 'y = -2x -2'
print(equation)
print(pattern.findall(equation))

print([equation] == pattern.findall(equation))


def input_equation(text):
    while True:
        string = input(text)
        try:
            if [string] != pattern.findall(string):
                raise ValueError
            return string
        except ValueError:
            print('Необходимо ввести уравнение вида: y = kx + b или y = -kx -b')


equation1 = input_equation('Введите уравнение №1').split()
equation2 = input_equation('Введите уравнение №2').split()


if int(equation1[2].replace('x', '')) == int(equation2[2].replace('x', '')):
    print('Прямые не пересекаются')
else:
    print('Прямые пересекаются')
