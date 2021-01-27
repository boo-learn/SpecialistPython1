# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n ⋅ m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.

# TODO: your code here

m_chock_size = int(input('Enter m-side: '))
n_chock_size = int(input('Enter n-side: '))
k = int(input('How much parts?: '))

break_size = 0
i = 1
while (m_chock_size * n_chock_size) % 2 == 0:
    if m_chock_size > n_chock_size:
        m_chock_size /= 2
    else: #возможно, что стороны будут равны, но при этом данное условие тоже работает
        n_chock_size /= 2

    i *= 2

print (m)


if i == k:
    print('Yes')
else:
    print('No')

#if ((i + 1) * 2) == (k * 2):
#    print('Yes')
#else:
#    print('No')
