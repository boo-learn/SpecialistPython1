# Бегун проводил ежедневные тренировки и записывал расстояния которые пробел за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)
dist_ft = [round(el / 3.28084, 2) for el in distances]
print(dist_ft)
