import pulp

# Створюємо задачу лінійного програмування (максимізація)
problem = pulp.LpProblem("Optimization_of_Production", pulp.LpMaximize)

# Змінні рішень: кількість виробленого лимонаду та фруктового соку
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Continuous")
fruit_juice = pulp.LpVariable("FruitJuice", lowBound=0, cat="Continuous")

# Цільова функція: максимізуємо загальну кількість вироблених продуктів
problem += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
# Вода: лимонад вимагає 2 од., фруктовий сік вимагає 1 од.
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

# Цукор: лимонад вимагає 1 од.
problem += 1 * lemonade <= 50, "Sugar_Constraint"

# Лимонний сік: лимонад вимагає 1 од.
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

# Фруктове пюре: фруктовий сік вимагає 2 од.
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язуємо задачу
problem.solve()

# Виводимо статус рішення
print(f"Status: {pulp.LpStatus[problem.status]}")

# Виводимо оптимальні значення кількості виробленого лимонаду та фруктового соку
print(f"Optimized Lemonade production: {lemonade.varValue}")
print(f"Optimized Fruit Juice production: {fruit_juice.varValue}")

# Виводимо загальну кількість вироблених напоїв
print(f"Total production: {lemonade.varValue + fruit_juice.varValue}")