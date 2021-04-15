# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
str_input, corr_input = "", False
while not corr_input:
    try:
        str_input = input("Введите данные: ")
    except (Exception, EOFError) as e:
        print(e)
        sys.exit()

    n, m = 0, 0
    try:
        values = str_input.split("x")
        n = float(values[0])
        m = float(values[1])
    except (NameError, ValueError, TypeError) as ev:
        print('Неверные значения')
    except Exception as e:
        print(e)
        sys.exit()

    corr_input = n and m

print(max(m, n) // min(m, n), "квадратов")
