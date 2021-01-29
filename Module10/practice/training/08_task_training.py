# Прочитав число из файла задачи 7, определите:
# Какие цифры встречаются в числе чаще всего?
# Если несколько цифр встречаются одинаковое максимальное кол-во раз - найди любые.
# Является ли данное число(20000-значное) четным?

# Читаем из файла
with open('num_dump.txt') as file:
  num_str = file.read()

#print('Длина числа: ', len(num_str))

# Преобразуем в список цифер
num_list = [int(num) for num in num_str]
# Делаем словарик: {цифра: количество}
num_dict = {num: num_list.count(num) for num in range(10)}
# print(num_dict)
# Находим максимальное
result = {k: v for k, v in filter(lambda x: num_dict[x[0]] == max(num_dict.values()), num_dict.items())}
print(result)

# Определёние чётности
if num_list[-1] % 2:
    print('Число не чётное')
else:
    print('Число чётное')
