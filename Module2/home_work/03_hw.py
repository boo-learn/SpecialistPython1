# пример:
# Входные данные
# 9.99
# Выходные данные
# 1 9.99 Rub.
# 2 19.98 Rub.
# 3 29.97 Rub.
# 4 39.96 Rub.
# 5 49.95 Rub.
# 6 59.94 Rub.
# 7 69.93 Rub.
# 8 79.92 Rub.
# 9 89.91 Rub.
# 10 99.90 Rub.
# 11 109.89 Rub.
# 12 119.88 Rub.
# 13 129.87 Rub.
# 14 139.86 Rub.
# 15 149.85 Rub.
# 16 159.84 Rub.
# 17 169.83 Rub.
# 18 179.82 Rub.
# 19 189.81 Rub.
# 20 199.80 Rub.

price = float(input('Введите цену товара:')) 
i = 0
while i < 20:
	i = i + 1
	sum = i * price
	if len(str(round((sum - int(sum)), 2))) == 4:
		print(i, sum, ' Rub.')
	else:
		print(i, str(sum) + '0', ' Rub.')
