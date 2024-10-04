# Объявляем функцию с 3-мя параметрами
# n- количество строк, m - количество столбцов, value - значение

def get_matrix(n, m, value):
    matrix = []  # пустой список
    for i in range(n):  # цикл для заполнения столбцов
        st = []  # пустая строка
        for j in range(m):
            st.append(value)  # цикл для заполнения строк
        matrix.append(st)  # добавляем заполненную строку в матрицу
    return matrix  # возвращаем заполненную матрицу


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
