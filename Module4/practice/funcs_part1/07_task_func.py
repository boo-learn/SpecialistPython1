# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def format_time(second):
    ss=second%60
    second=second//60
    mm = second % 60
    second = second // 60
    hh=second
    list_time=hh,mm,ss
    return list_time
    #print(list_time)

sec=29143

print(f"{format_time(sec)[0]:0>2}:{format_time(sec)[1]:0>2}:{format_time(sec)[2]:0>2}")
