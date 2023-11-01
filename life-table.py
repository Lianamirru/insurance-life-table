import math

with open('death.txt', 'r') as file:
    lines = file.readlines()

base = 1000000
life_table_root = 100000

# filter fields
year = '2020'
reg = '1100'
group = 'T'
sex = 'M'

displayed_data = []
data = []

for line in lines:
    rows = line.split(',')  # Предполагаем, что столбцы разделены пробелами
    if len(rows) > 1 and rows[0] == year and rows[1] == reg and rows[2] == group and rows[3] == sex:
        data.append(rows)
        displayed_data.append(line)

with open('data.txt', 'w') as file:
    file.writelines(displayed_data)

# data_dx = [(1-math.exp(-int(value)/base))*life_table_root for value in data[0][4:]]
data_dx = [(int(value)/base)*life_table_root for value in data[0][4:]]

print(len(data_dx))


# Создаем списки для lx и dx
lx = [100000]  # Изначальное количество человек
dx = []  # Количество умерших на каждом возрасте

for dx_value in data_dx:
    lx_value = lx[-1]
    lx.append(lx_value - dx_value)
    dx.append(dx_value)

print(lx)

with open('mortality_table_lx.txt', 'w') as file:
    file.write("возраст lx\n")
    for age, lx_value in enumerate(lx):
        file.write(f"{age} {lx_value}\n")

import matplotlib.pyplot as plt

# Данные о возрасте и dx
ages = list(range(len(dx))
dx_values = dx

# Создаем график
plt.figure(figsize=(10, 6))
plt.plot(ages, dx_values, marker='o', linestyle='-', color='b')

# Настройка графика
plt.title('График dx относительно возраста')
plt.xlabel('Возраст')
plt.ylabel('dx')
plt.grid(True)

# Отображаем график
plt.show()