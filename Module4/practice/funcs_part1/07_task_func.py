# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43


def sec_to_hour_minute_sec(sec_num):
    hours = sec_num // 3600
    minutes = (sec_num % 3600) // 60
    seconds = (sec_num % 60) % 60
    return f'{"0" + str(hours) if hours < 10 else str(hours)}:{"0" + str(minutes) if minutes < 10 else str(minutes)}:' \
           f'{"0" + str(seconds) if seconds < 10 else str(seconds)}'


print(sec_to_hour_minute_sec(3661))
