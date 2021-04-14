# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def time (sec):
    min = sec // 60
    hours = min // 60
    min = min % 60
    sec = sec % 60
    hours = str(hours).zfill(2)
    min = str(min).zfill(2)
    sec = str(sec).zfill(2)
    print (f'{hours}:{min}:{sec}')

time(29143)
