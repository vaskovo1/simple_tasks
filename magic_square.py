"""
Магическим квадратом порядка nnn называется квадратная таблица размера n×n, составленная из всех чисел
1,2,3,…,n**2, так, что суммы по каждому столбцу, каждой строке и каждой из двух
диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица
магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы
матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.


Sample Input 1:

3
8 1 6
3 5 7
4 9 2

Sample Output 1:

YES

Sample Input 2:

3
8 2 6
3 5 7
4 9 1

Sample Output 2:

NO

Sample Input 3:

3
4 9 2
3 5 7
8 1 6

Sample Output 3:

YES


"""

n = int(input())

matrix = []
mas = []
flag_all_digits = True
flag_rows = True
flag_cols = True
flag_diag_main = True
flag_diag_side = True
flag_no_zero = True
total_diag_main = 0
total_diag_side = 0

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    mas.extend(row)

digit_sum = sum(matrix[0])

if 0 in mas:
    flag_no_zero = False

res_set = set(mas)

if res_set != set(list(range(1, n ** 2 + 1))):
    flag_all_digits = False

for i in range(n):
    if sum(matrix[i]) != digit_sum:
        flag_rows = False
        break
    total = 0

    for j in range(n):
        total += matrix[j][i]
    if total != digit_sum:
        flag_cols = False
        break

    total_diag_main += matrix[i][i]
    total_diag_side += matrix[i][n-1-i]


if total_diag_main != digit_sum:
    flag_diag_main = False
elif total_diag_side != digit_sum:
    flag_diag_side = False

print('YES' if all([flag_all_digits, flag_rows, flag_cols, flag_diag_main, flag_diag_side, flag_no_zero]) else 'NO')