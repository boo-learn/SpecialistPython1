# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

from os import path
from settings import BASE_DIR
import re

with open(path.join( BASE_DIR,"data","info.txt"), "r", encoding="utf-8") as f:
    lst=list(line.rstrip() for line in f if not line.rstrip().isalpha())
    summ=sum(int(re.search("\-?[0-9]+",el).group(0)) for el in lst)
print(lst)
print(summ)
