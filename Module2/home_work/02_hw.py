# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here

n = int(input("n ="))
one = n % 10
dec = n // 10 % 10
if one == 1 and dec != 1:
  print   ("корова")
elif 2 <= one <= 4 and dec != 1:
  print("коровы")
else:
  print("коров")
  
#СПИСАЛ :))
