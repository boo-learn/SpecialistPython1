# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def str_time(sec_total):
    m_total = sec_total // 60
    ss = sec_total - m_total * 60
    hh = m_total // 60
    mm = m_total - hh * 60
    return f"{hh:0>2}:{mm:0>2}:{ss:0>2}"
