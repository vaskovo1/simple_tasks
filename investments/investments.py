"""
Вам доступен файл data.csv, который содержит информацию об инвестициях в различные стартапы. В первом столбце записано
название компании (стартапа), во втором — инвестируемая сумма, в третьем — валюта, в четвертом — раунд инвестиции:

company,raisedAmt,raisedCurrency,round
LifeLock,6850000,USD,b
LifeLock,6000000,USD,a
LifeLock,25000000,USD,c
MyCityFaces,50000,USD,seed
Flypaper,3000000,USD,a
...

Напишите программу с использованием конвейеров генераторов, определяющую общую сумму, которая была инвестирована в
раунде а, и выводящую полученный результат.
"""

from csv import reader

with open('data.csv', 'r', encoding='utf-8') as file:
    str_am = (line[1] for line in reader(file) if line[-1] == 'a')
    final_sum = sum(map(int, str_am))
    print(final_sum)
    