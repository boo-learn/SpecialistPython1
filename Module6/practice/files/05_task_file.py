# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
h = open("data\hours_of.txt", "r", encoding="utf-8")

for line in h:
    if line[-2:-1].isdigit():
        line2 = line.split()
        name = line2[0]
        surname = line2[1]
        hours = int(line2[2])
        w = open("data\workers.txt", "r", encoding="utf-8")
        for el in w:
            if el[-2:-1].isdigit():
                worker_line = el.split()
                if name == worker_line[0] and surname == worker_line[1]:
                    print(worker_line[0], worker_line[1], "earned for month:")
                    norm_hours = int(worker_line[4])
                    month_payment = int(worker_line[2])
                    if hours >= norm_hours:
                        payment = month_payment + month_payment*(hours-norm_hours)*2/norm_hours
                    else:
                        payment = month_payment*hours/norm_hours
                    print("Payment:", payment)
        w.close()
