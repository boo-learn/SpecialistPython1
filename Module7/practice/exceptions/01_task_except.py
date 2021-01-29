# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
while True:
    try:
        string = input("input <number1>x<number2>: ")
        #print(string.split("x"))
        n = float(string.split("x")[0])
        m = float(string.split("x")[1])
        # print("n =", n, "\tm =", m)
        # print(m>n)
        break
    except ValueError:
        print("incorrect values..\n try again")

if m > n:
    print("0 squares")
else:
    print(round(n//m), "squares"
