"""
Реализуйте функцию get_biggest(), которая принимает один аргумент:

    numbers — список целых неотрицательных чисел

Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
Если список numbers пуст, функция должна вернуть число −1.

Примечание. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа:
123,132,213,231,312,321. Наибольшим из представленных является 321.
"""


def get_biggest(lst):
    if not lst:
        return -1
    len_biggest_num = max(list(map(len, list(map(str, lst)))))
    lst.sort(key=lambda x: str(x) * len_biggest_num, reverse=True)
    return int(''.join(str(i) for i in lst))


print(get_biggest([1, 2, 3]))  # 321
print(get_biggest([61, 228, 9, 3, 11]))  # 961322811
print(get_biggest([7, 71, 72]))  # 77271
print(get_biggest([]))  # -1
print(get_biggest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # 987654321100
