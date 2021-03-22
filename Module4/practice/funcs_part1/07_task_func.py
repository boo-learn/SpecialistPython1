# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def null(i):
    v = i
    if v < 10:
        return (f"0{v}")
    else:
        return (v)

def time(s):
    hh = s // 3600
    mm = s % 3600 // 60
    ss = s % 3600 % 60
    if hh == 0 and mm == 0:
        return(f"00:00:{null(ss)}")
    elif hh == 0 and mm != 0:
            return(f"00:{null(mm)}:{null(ss)}")
    elif hh != 0 and mm != 0:
            return (f"{null(hh)}:{null(mm)}:{null(ss)}")

print(time(29143))
