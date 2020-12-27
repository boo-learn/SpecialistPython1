# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

i = 0
while i==0:
 input_data = input("input  data in format 12x6")

 a = input_data.split("x")

 if(a[0].isdigit() and a[1].isdigit() and len(a)==2):
  print(a);
  i=1
 else:
    print("wrong")
    
    
    ###################
    
    i = 0
while i == 0:
    try:
        input_data = input("input  data in format 12x6")

        a = input_data.split("x")

        log1 = a[0].isdigit()

        log2 = a[1].isdigit()
        log3 = len(a) == 2
        i=1
    except ValueError:
     print("wrong ")
