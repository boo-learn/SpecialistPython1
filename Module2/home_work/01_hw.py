# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Формат входных данных
# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n ⋅ m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.

n = int(input('Введите n: '))
m = int(input('Введите m: '))
k = int(input('Введите k: '))

if k == m or k == n:
    print('YES')
else:
    print('NO')
