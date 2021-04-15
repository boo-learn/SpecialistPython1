# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
employees = {}

f_staff = open("data/workers.txt", "r", encoding="utf-8")
header = f_staff.readline()
for line in f_staff:
    data = line.split()
    name_key = data[1] + "_" + data[0]
    employees[name_key] = {"salary": float(data[2]), "normal_hours": float(data[4]), "actual_hours": 0, "pay": 0}
f_staff.close()

f_timesheet = open("data/hours_of.txt", "r", encoding="utf-8")
header = f_timesheet.readline()
for line in f_timesheet:
    data = line.split()
    name_key = data[1] + "_" + data[0]
    if employees.get(name_key) is not None:
        employees[name_key]["actual_hours"] = float(data[2])
f_timesheet.close()

total_pay = 0
for employee in employees.values():
    if employee["actual_hours"] < employee["normal_hours"]:
       employee["pay"] = round(employee["salary"] * employee["actual_hours"] / employee["normal_hours"], 2)
    elif employee["actual_hours"] > employee["normal_hours"]:
        employee["pay"] = round(employee["salary"] + (employee["salary"] / employee["normal_hours"]) * 2 * (employee["actual_hours"] - employee["normal_hours"]), 2)
    else:
        employee["pay"] = employee["salary"]
    total_pay += employee["pay"]

print(employees)
print(total_pay)
