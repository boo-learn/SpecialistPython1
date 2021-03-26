# Бегун проводил ежедневные тренировки и записывал расстояния которые пробел за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)

feet_koeff = 3.28084

distances_feets = []

"""
# using "simple for" cycle:

for el in distances:
    distances_feets.append(float(float(el)*feet_koeff))
"""

distances_feets = list(map(lambda el: el * feet_koeff, distances))

print(distances)
print(distances_feets)
