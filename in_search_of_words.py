"""
Дана последовательность слов. Напишите программу, которая выводит наиболее часто встречаемое слово в этой
последовательности. Если таких слов несколько, программа должна вывести то, которое больше в лексикографическом
сравнении.

Формат входных данных
На вход программе подается последовательность слов, разделенных пробелом.

Формат выходных данных
Программа должна определить наиболее часто встречаемое слово в введенной строке и вывести его в нижнем регистре. Если
таких слов несколько, программа должна вывести то, которое больше в лексикографическом сравнении, так же в нижнем в
регистре.

Примечание 1. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

Арбуз Малина арбуЗ Клубника арбуз банан малина черешня вишня арбуз клубника Банан

Sample Output 1:

арбуз

Sample Input 2:

МаЛиНа клубника Арбуз банаН Малина Черешня вишня арбуз клубника банан

Sample Output 2:

малина

"""

from collections import Counter

c = Counter(input().lower().split())

print(sorted(c.most_common(), key=lambda tp: (tp[1], tp[0]), reverse=True)[0][0])