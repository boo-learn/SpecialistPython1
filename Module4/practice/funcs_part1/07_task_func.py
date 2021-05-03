# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def time(secs):
    hh=str(secs//3600)
    mm=str((secs-int(hh)*3600)//60)
    ss=str(secs-int(hh)*3600-int(mm)*60)
    return hh.rjust(2, '0')+":"+mm.rjust(2, '0')+":"+ss.rjust(2, '0')
print(time(29143))
