# Бегун проводил ежедневные тренировки и записывал расстояния которые пробел за занятия в метрах:

distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]


def foot(a):
    b = round(3.2808 * a, 2)
    return b


foot_distances = map(foot, distances)
print(list((foot_distances)))
