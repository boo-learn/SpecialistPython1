# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def split60(n):
    return (n % 60, n // 60)


def format_time(seconds):
    sec, minutes = split60(seconds)
    minutes, hours = split60(minutes)

    return "{}:{}:{}".format(hours, minutes, sec)


print(format_time(456356))
