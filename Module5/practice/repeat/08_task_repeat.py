# Вы решили сделать вклад в банк некоторой суммы на n лет.
# Банк вам предложил x% годовых с расчетом по простым процентам или
# y% годовых по сложным % с периодом капитализации 1 месяц.
# При заданных процентных ставках, определите какой из вкладов вам выгоднее на 5 лет.
# Примечание: формулы расчета простых и сложных процентов ищите на гуглодиске в папке с материалами.
def deposit(x, a, n):
    for i in range(1,n+1):
        x+=x*(a/100)
    return x

def deposit_compl(x, a, n):
    n=n*12
    a=a/100/12
    for i in range(1,n+12):
        x+=x*a
def deposit_compare(a, x,y, n):
    if deposit(a,x,n)>deposit_compl(a,y,n):
        return "Выгоднее обычный"
    return "Выгоднее сложный"
