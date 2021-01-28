# "Банкомат"
# В банкомате есть купюры 5000, 2000, 1000 и 500 рублей.
# Напишите функцию, которая будет рассчитывать количество купюр, которыми можно будет выдать
# запрошенную пользователем сумму и возвращать ее в виде словаря, ключами в котором будут номиналы банкнот,
# а значениями кол-во банкнот. Если пользователь запросил некорректную сумму,
# нужно вывести дружественное сообщение об ошибке.
# Результат работы программы - текстовый отчет о номиналах и количестве купюр.

cash_dict = {5000:0, 2000:0, 1000:0, 500:0}

def get_cash(in_data:int):
    if in_data % list(cash_dict.keys())[-1] != 0:
        print(f'Сумма должна быть кратна {list(cash_dict.keys())[-1]}')
        raise ValueError

    for cash_lim in cash_dict:
        cash_dict[cash_lim] = in_data // cash_lim
        in_data -= cash_lim * cash_dict[cash_lim]

    return cash_dict

while True:
    try:
        req_cash = int(input(f'Введите сумму кратную кратную {list(cash_dict.keys())[-1]}: '))
        result_cash_dict = get_cash(req_cash)
    except ValueError as err:
        print('Ошибка ввода! Пожалуйста попробуй ещё раз! ')
    else:
        break

print('Вы получите: ')
for cash_lim in cash_dict:
    if cash_dict[cash_lim] != 0:
        print(f'купюры {cash_lim} - {cash_dict[cash_lim]} шт.')
