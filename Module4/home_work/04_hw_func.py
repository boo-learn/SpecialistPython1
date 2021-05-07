# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
import math


def parse(expression):
    val = []
    op = []
    res_val = []
    tokens = expression.split(" ")
    for token in tokens:
        if token == "+" or token == "-":
            op.append(token)
        else:
            val.append(token)
    expression += " +"  # чтобы корректно обработать последнее
    flag = False  # лежит ли слева от того пробела, на котором мы стоим, уже обработанная дробная часть
    left_side = 0  # левое число в списке val по отношению к текущему пробелу
    for i, ch in enumerate(expression):
        if ch == " ":
            if flag:  # если слева обработанная дробная
                flag = False
                continue
            l_ch = expression[i - 1]
            r_ch = expression[i + 1]
            if l_ch != "+" and l_ch != "-" and r_ch != "+" and r_ch != "-":  # и слева, и справа цифра,
                # т.е. стоим внутри дроби
                res_val.append(make_composed_fraction(val[left_side], val[left_side + 1]))
                flag = True
                if left_side + 2 < len(val):  # если дробное не самое последнее
                    left_side += 2
            elif l_ch != "+" and l_ch != "-":  # если слева число (и не уже обработанное дробное), а справа — знак
                res_val.append(make_composed_fraction(val[left_side]))
                if left_side + 1 < len(val):  # если число не самое последнее
                    left_side += 1
    return res_val, op


def make_composed_fraction(*args):
    tokens = args[-1].split("/")
    if len(tokens) == 1:  # если пришло только целое число
        return int(tokens[0]), 1
    if len(args) == 1:  # если пришла только дробь
        return int(tokens[0]), int(tokens[1])
    integer = int(args[0])
    sign = 1
    if integer < 0:
        sign = -1
    return integer * int(tokens[1]) + sign * int(tokens[0]), int(tokens[1])


# Наименьшее общее кратное
def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def print_fraction(fraction):
    sign = ""
    if fraction[0] == -1:
        sign = "-"
    if fraction[1] == 0 and fraction[2] == 0:
        print("0")
    elif fraction[1] == 0:
        print(f"{sign}{fraction[2]}/{fraction[3]}")
    elif fraction[2] == 0:
        print(f"{sign}{fraction[1]}")
    else:
        print(f"{sign}{fraction[1]} {fraction[2]}/{fraction[3]}")


def calc(expression):
    val, op = parse(expression)

    s = [0, 1]
    op.insert(0, "+")  # сложение изначального s с первым числом
    for i, fraction in enumerate(val):
        sign = 1
        if op[i] == "-":
            sign = -1
        denominator_l = s[1]
        denominator_r = fraction[1]
        common_denominator = lcm(denominator_l, denominator_r)
        missing_coef_l = common_denominator / denominator_l  # на сколько нужно домножить числители
        missing_coef_r = common_denominator / denominator_r
        s[0] = s[0] * int(missing_coef_l) + sign * fraction[0] * int(missing_coef_r)  # итоговый числитель
        s[1] = common_denominator

    sign = 1
    if s[0] < 0:
        sign = -1
        s[0] = abs(s[0])
    integer = s[0] // s[1]
    numerator = s[0] - integer * s[1]
    gcd = math.gcd(numerator, s[1])
    numerator /= gcd
    denominator = s[1] / gcd
    return sign, integer, int(numerator), int(denominator)


expr = "-2/3 - -2 + 3/5 + 1 1/15"
res = calc(expr)
print_fraction(res)
