"""
Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один
аргумент:

    dates — список строковых дат в формате DD.MM.YYYY

Функция должна возвращать список, в котором содержатся все даты из списка dates,
расположенные в порядке возрастания, а также все недостающие промежуточные
даты.

Например, если список dates содержит период с 01.11.2021 по 07.11.2021:

dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

в котором отсутствуют даты 02.11.2021, 05.11.2021, 06.11.2021. Тогда вызов
функции:

fill_up_missing_dates(dates)

должен вернуть список:

['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021',
'06.11.2021', '07.11.2021']

Функция должна создавать и возвращать новый список, а не изменять переданный.
"""

from datetime import datetime, timedelta


def fill_up_missing_dates(d):
    pattern = '%d.%m.%Y'
    dates = set([datetime.strptime(date, pattern) for date in d])
    td = max(dates) - min(dates)

    for i in range(1, td.days):
        dates.add(min(dates) + timedelta(days=i))

    res = [date.strftime(pattern) for date in sorted(dates)]

    return res


some_dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(some_dates))

