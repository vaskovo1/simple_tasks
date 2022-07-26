"""
Вам доступен файл deniro.csv, каждый столбец которого содержит либо только
числа, либо только слова:

Machete,2010,72
Marvin's Room,1996,80
Raging Bull,1980,97
...

Напишите программу, которая сортирует содержимое данного файла по указанному
столбцу. Причем данные должны быть отсортированы в порядке возрастания чисел,
если столбец содержит числа, и в лексикографическом порядке слов, если столбец
содержит слова.
На вход программе подается натуральное число — номер столбца файла deniro.csv.

Нумерация столбцов начинается с единицы.
Если две какие-либо строки имеют одинаковые значения в столбцах, то следует
сохранить их исходный порядок следования.
Разделителем в файле deniro.csv является запятая, при этом кавычки не
используются.
"""

import csv


def sorting(lst):
    if lst[col].isdigit():
        return int(lst[col])
    return lst[col]


col = int(input()) - 1

with open('deniro.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    table = [row for row in rows]
    table.sort(key=sorting)

[print(*row, sep=',') for row in table]
