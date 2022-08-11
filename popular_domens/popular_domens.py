"""
Вам доступен файл data.csv, который содержит неповторяющиеся данные о
пользователях некоторого ресурса. В первом столбце записано имя пользователя,
во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...

Напишите программу, которая создает файл domain_usage.csv, имеющий следующее
содержание:

domain,count
rambler.ru,24
iCloud.com,29
...

где в первом столбце записано название почтового домена, а во втором —
количество пользователей, использующих данный домен. Домены в файле должны
быть расположены в порядке возрастания количества их использований, при
совпадении количества использований — в лексикографическом порядке.
"""

import csv

dct = {}
columns = ['domain', 'count']

with open('data.csv', encoding='utf-8') as f:
    rows = csv.DictReader(f, delimiter=',')
    for row in rows:
        dct[row['email'].split('@')[1]] = dct.get(row['email'].split('@')[1], 0) + 1

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as wf:
    writer = csv.writer(wf, delimiter=',')
    writer.writerow(columns)
    for k,v in sorted(dct.items(), key=lambda x: (int(x[1]), x[0])):
        writer.writerow([k, v])