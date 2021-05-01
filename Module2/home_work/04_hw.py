# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

while True:                                 # Для повторного запуска программы без выхода

    a = int(input("сторона квадрата = "))   #Проверка входных данных для себя
    if a <= 2 or a > 30:
        print("error")

    i = 1
    while i <= a:
        if i == 1 or i == a:
            print( a*"#" )
        else:
            print( "#" + ( a - 2 )*" " + "#" )
        i += 1        
        
    if input(" Закончить: 'пробел' и 'Enter'  |  еще раз: 'Enter'") == " ": # Для повторного запуска программы без выхода
        break
