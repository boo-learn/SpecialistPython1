# Вы решили сделать вклад в банк некоторой суммы на n лет.
# Банк вам предложил x% годовых с расчетом по простым процентам или
# y% годовых по сложным % с периодом капитализации 1 месяц.
# При заданных процентных ставках, определите какой из вкладов вам выгоднее на 5 лет.
# Примечание: формулы расчета простых и сложных процентов ищите на гуглодиске в папке с материалами.
def deposit_simple(x, a, n):
    for _ in range(n):
        x += x*a/100
    return x


def deposit_compound(x, a, n):
    x = x*(1+(a/100)/12)**(n*12)
    return x


money = int(input('Денег: '))
percent_simple = int(input('Простой процент годовых: '))
percent_compound = int(input('Сложный процент годовых: '))
years = int(input('Лет: '))
# years = 5

print('По простому проценту', deposit_simple(money, percent_simple, years))
print('По сложному проценту', deposit_compound(money, percent_compound, years))
