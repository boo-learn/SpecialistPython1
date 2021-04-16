# Одноклеточная амеба каждые 3 часа делится на 2 такие же амёбы.
# Необходимо определить, сколько будет амеб через n часов, если первоначально была только одна амёба.
# Формат входных данных: Вводится целое число n (3≤n≤90).
# Формат выходных данных: Требуется одно число — конечное число амеб.
def count_amoebas(n):
    if n < 3:
        return amoebas
    else:
        return count_amoebas(n - 3) * 2


amoebas = 1
while True:
    try:
        hours = int(input('Введите количество часов: '))
        if hours > 90 or hours < 3:
            raise ValueError
        break
    except (ValueError, TypeError):
        print('Необходимо ввести целое количество амеб в диапазоне 3≤n≤90')

print(count_amoebas(hours))
