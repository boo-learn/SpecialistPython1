# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
t=False
while(t!=True):
    s=input('NxM')
    try:
        n=0
        m=0
        n=s[:s.find('x')]
        m=s[s.find('x')+1:]
        print(int(n)/int(m))
        t=True
    except ValueError:
        print('Format error')
