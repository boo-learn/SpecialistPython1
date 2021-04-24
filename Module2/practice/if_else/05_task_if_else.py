# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

m = int(input('Input here: '))
if m == 1:
	print('Yanuary')
if m == 2:
	print('February')
if m == 3:
	print('March')
if m == 4:
	print('April')
if m == 5:
	print('May')
if m == 6:
	print('June')
if m == 7:
	print('July')
if m == 8:
	print('August')
if m == 9:
	print('September')
if m == 10:
	print('October')
if m == 11:
	print('November')
else:
	print('December')
