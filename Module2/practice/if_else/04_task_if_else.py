# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

int_num = int(input('целое число: '))
if int_num % 5 == 0 and int_num % 3 == 0:
    print('Foobar')
elif int_num % 5 != 0 or int_num % 3 != 0:
    if int_num % 5 == 0:
        print('Bar')
    elif int_num % 3 == 0:
        print('Foo')
