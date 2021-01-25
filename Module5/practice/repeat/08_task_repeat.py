# Вы решили сделать вклад в банк некоторой суммы на n лет.
# Банк вам предложил x% годовых с расчетом по простым процентам или
# y% годовых по сложным % с периодом капитализации 1 месяц.
# При заданных процентных ставках, определите какой из вкладов вам выгоднее на 5 лет.
# Примечание: формулы расчета простых и сложных процентов ищите на гуглодиске в папке с материалами.

def simple_deposit(init_val, rent, years):
    return init_val*(1 + years*(rent/100))

def complex_deposit(init_val, year_rent, period_num, years):
    return init_val*(1 + year_rent/(period_num*100))**(period_num*years)

percents = 10

simple_result = simple_deposit(100000, 10, 5)
complex_result = complex_deposit(100000, 10, 12, 5)

print('по простым процентам:', simple_result)
print("по сложным процентам: %.02f" % (complex_result))

if simple_result > complex_result:
    print('ставка по простым процентам выгодней')
else:
    print('ставка по сложным процентам выгодней')
