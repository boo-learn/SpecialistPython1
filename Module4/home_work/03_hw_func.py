# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def distance(x1, y1, x2, y2):
     return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5

x1=int(input('enter x1: '))
y1=int(input('enter y1: '))
R1=int(input('enter r1: '))
x2=int(input('enter x2: '))
y2=int(input('enter y2: '))
R2=int(input('enter r2: '))


print ('Yes') if distance (x1,y1,x2,y2) <= R1 + R2 else print('No')
