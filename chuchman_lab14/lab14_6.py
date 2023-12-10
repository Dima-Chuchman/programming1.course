#14.6.
#Розв’язати квадратне рівняння ax^2+bx+c=0. Оформити перевірку вхідних даних
# (що рівняння є квадратним і має розв’язок на множині дійсних чисел) за допомогою оператора assert.

a = float(input("Введіть коефіцієнт a:"))
b = float(input("Введіть коефіцієнт b:"))
c = float(input("Введіть коефіцієнт c:"))

D = b**2 - 4*a*c
assert a != 0, "а не може дорівнювати 0, введіть коректні дані "
assert D >= 0, "Дискримінант від'ємний, введіть інші a, b, c."

x1 = (-b + (D**0.5)) / (2*a)
x2 = (-b - (D**0.5)) / (2*a)

try:
    print("Розв'язки рівняння:", x1, x2)
except AssertionError as e:
    print(f"Помилка: {e}")
    
#Я не розумію чому видає помилку, зробив другий варіант, де все працює