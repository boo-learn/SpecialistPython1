# Напишите функцию, принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def sec4str(seconds):
    sec_val = seconds % (24 * 3600)
    hour_val = sec_val // 3600
    sec_val %= 3600
    min_val = sec_val // 60
    sec_val %= 60

    hour_val = str(hour_val)
    if len(hour_val) == 1:
        hour_val = "0" + hour_val

    min_val = str(min_val)
    if len(min_val) == 1:
        min_val = "0" + min_val

    sec_val = str(sec_val)
    if len(sec_val) == 1:
        sec_val = "0" + sec_val

    print(f"{hour_val}:{min_val}:{sec_val}")


seconds = 29143
sec4str(seconds)





