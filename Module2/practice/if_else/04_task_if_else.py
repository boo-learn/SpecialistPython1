# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here
num = int(input('input number: '))

if num%3 == 0 and num%5 == 0 and num != 0:
    print('foobar')
elif num%5 == 0 and num != 0:
    print('bar')
elif num%3 == 0 and num != 0:
    print('foo')
