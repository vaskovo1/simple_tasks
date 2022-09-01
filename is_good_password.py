"""
Назовем пароль хорошим, если

    его длина равна 999 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

    string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.
"""


def is_good_password(string):
    if len(string) >= 9:
        if set([str(i) for i in range(10)]) & set(string):
            if string.lower() != string and string.upper() != string:
                return True
    return False



