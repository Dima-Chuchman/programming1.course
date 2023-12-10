#T.10.1
#Описати модуль роботи з квадратними матрицями та векторами.
#Реалізувати дії: 1)Ввести матрицю. 2)Вивести матрицю. 3) Множення матриць. 4)Множення матриць на вектор.
# 5)Множення матрицю на матрицю. 6)Переставлення рядків матриці. 7)Переставлення стовпчиків матриці.
# 8)Отримання рядка матриці. 9)Множення вектора на число. 10)Віднімання вектора.
# З використанням модуля розв'язати задачі:
# a)Перетворити матрицю у верхню трикутну лінійними перетвореннями.
# б) Визначити ранг матриці.
# в) Обчислити визначник матриці.


def multiplication_matrix(matrix1, matrix2):     #Множення матриць
    mult_matrix = []
    for i in range(len(matrix1)):
        row_mult = []
        for j in range(len(matrix2[0])):
            result = 0
            for k in range(len(matrix2)):
                result += matrix1[i][k] * matrix2[k][j]
            row_mult.append(result)
        mult_matrix.append(row_mult)
    return mult_matrix


def matrix_vector_multiplication(matrix, vector):  #Перевірка вектора.Множення
    if len(matrix1[0]) != len(vector):
        return
    
    mult_vector = []
    for i in range(len(matrix)):
        result = 0
        for j in range(len(vector)):
            result += matrix[i][j] * vector[j]
        mult_vector.append(result)
    return mult_vector

# Перша матриця---------------------->

while True:
    try:
        n = int(input("Введіть розмірність квадратної матриці номер 1 : ")) #Введення розмірності матриці
        if n <= 0:
            raise ValueError("Введіть натуральне число більше за 0")
        break
    except ValueError:
        print("Введіть натуральне число більше за 0")

matrix1 = []

for i in range(n):
    row1 = []
    for j in range(n):
        while True:
            try:
                element1 = int(input(f"Введіть елемент [{i + 1}][{j + 1}]: ")) #Введення елементів матриці
                row1.append(element1)
                break
            except ValueError:
                print("Введіть ціле число: ")
    matrix1.append(row1)
    
# Друга матриця---------------------->

while True:
    try:
        n = int(input("Введіть розмірність квадратної матриці номер 2 : "))  # Введення розмірності матриці
        if n <= 0:
            raise ValueError("Введіть натуральне число більше за 0")
        break
    except ValueError:
        print("Введіть натуральне число більше за 0")

matrix2 = []

for i in range(n):
    row2 = []
    for j in range(n):
        while True:
            try:
                element2 = int(input(f"Введіть елемент [{i + 1}][{j + 1}]: "))  # Введення елементів матриці
                row2.append(element2)
                break
            except ValueError:
                print("Введіть ціле число: ")
    matrix2.append(row2)

while True:
    question = input("""\nОберіть подальші дії над матрицями:
    1)Для того щоб продовжити, оберіть цифру 1
    2)Щоб завершити, оберіть цифру 2
    Ваш вибір: """)
    if question == '1':
        while True:
            other_actions = input("""\nОберіть дію над матрицями:
            1)Множення матриць
            2)Множення на вектор
            Ваш вибір: """)
            
            if other_actions == '1':
                result_matrix = multiplication_matrix(matrix1, matrix2)
                print("Результат множення матриць: ")
                for row in result_matrix:
                    print(row)
                break
                
            elif other_actions == '2':
                while True:
                    try:
                        vector_size = int(input("Введіть розмірність вектора (повинна дорівнювати кількості стовпців у матриці): "))
                        if vector_size <= 0 or vector_size != n:
                            raise ValueError(f"Розмірність вектора повинна бути натуральним числом більше за 0 і співпадати з кількістю стовпців у матриці ({n})")
                        
                        vector = []
                        
                        for i in range(vector_size):
                            while True:
                                try:
                                    numberes = int(input(f"Введіть значення для елементу {i + 1} вектора: "))
                                    vector.append(numberes)
                                    break
                                except ValueError:
                                    print("Введіть число: ")
                        
                        result_mult_vector1 = matrix_vector_multiplication(matrix1, vector)
                        break
                    except ValueError as e:
                        print(e)
                print("Результат множення першої матриці на вектор: ", result_mult_vector1)
                
    elif question == '2':
        print("Квадратна матриця 1 : ")  # Вивід матриці
        for row in matrix1:
            print(row)
        
        print("Квадратна матриця 2 : ")  # Вивід матриці
        for row in matrix2:
            print(row)
        break
    else:
        print()
