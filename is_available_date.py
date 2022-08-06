"""
Даны:
    booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата,
    либо период (две даты через дефис). Например:

    ['04.11.2021', '05.11.2021-09.11.2021']

    date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает
    забронировать номер. Например:

    '01.11.2021' или '01.11.2021-04.11.2021'

Напишите функцию is_available_date, которая принимает 2 вышеупомянутых аргумента и возвращает True, если есть
возможность забронировать дату, и False - в противном случае
"""

from datetime import datetime


def is_available_date(booked_dates, date_for_booking):
    for d in booked_dates:
        if '-' not in d:
            bd.add(datetime.strptime(d, '%d.%m.%Y'))
        else:
            date1, date2 = d.split('-')
            d1 = int(date1[:2])
            d2 = int(date2[:2])
            for day in range(d1, d2 + 1):
                new_date = str(day) + date1[2:]
                bd.add(datetime.strptime(new_date, '%d.%m.%Y'))

    if '-' not in date_for_booking:
        dfb.add(datetime.strptime(date_for_booking, '%d.%m.%Y'))
    else:
        date1, date2 = date_for_booking.split('-')
        d1 = int(date1[:2])
        d2 = int(date2[:2])
        for day in range(d1, d2 + 1):
            new_date = str(day) + date1[2:]
            dfb.add(datetime.strptime(new_date, '%d.%m.%Y'))

    if bd & dfb:
        return False
    return True

bd = set()
dfb = set()

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))