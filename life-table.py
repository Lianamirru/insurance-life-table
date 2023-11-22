import matplotlib.pyplot as plt
import math

with open('death.txt', 'r') as file:
    death_rows = file.readlines()

with open('population.txt', 'r') as file:
    population_rows = file.readlines()


base = 1000000
life_table_root = 100000

# filter fields
year = '2015'
reg = '1100'
group = 'T'
sex = 'B'

# death_rate
filtered_death_display = []
filtered_death = []

for death_row in death_rows:
    rows = death_row.split(',')
    if len(rows) > 1 and rows[0] == year and rows[1] == reg and rows[2] == group and rows[3] == sex:
        filtered_death.append(rows)
        filtered_death_display.append(death_row)

with open('filtered_death.txt', 'w') as file:
    file.writelines(filtered_death_display)

# population
filtered_population_display = []
filtered_population = []

for population_row in population_rows:
    rows = population_row.split(',')
    if len(rows) > 1 and rows[0] == year and rows[1] == reg and rows[2] == group and rows[3] == sex:
        filtered_population.append(rows)
        filtered_population_display.append(population_row)

with open('filtered_population.txt', 'w') as file:
    file.writelines(filtered_population_display)

# data_dx = [(1-math.exp(-int(value)/base))*life_table_root for value in filtered_death[0][4:]]
# data_dx = [(int(value)/base)*life_table_root for value in filtered_death[0][4:]]
death_quants = []
filtered_population = filtered_population[0][4:]
filtered_death = filtered_death[0][4:]


for index in range(len(filtered_population)-1):
    print(filtered_death)

    death_quants.append(
        int(filtered_death[index])/base*int(filtered_population[index]))

sum_death = sum(death_quants)

data_dx = []
for death_quant in death_quants:
    data_dx.append(death_quant/sum_death*life_table_root)
    # Mx = death_quant/sum_death
    # data_dx.append((Mx/(2+Mx))*life_table_root)


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


# Данные о возрасте и dx
ages = list(range(len(dx)))
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
