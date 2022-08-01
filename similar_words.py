"""
Напишите программу, которая находит все схожие слова для заданного слова.
Слова называются схожими, если имеют одинаковое количество и расположение
гласных букв. При этом сами гласные могут различаться.

На вход программе подается одно слово, записанное в первой строке,
затем натуральное число n — количество слов для сравнения и n строк со словами.

Программа должна вывести все схожие слова для заданного слова,
сохранив их исходный порядок следования.

Sample Input:

машина
8
сеть
машинист
дорога
урок
работа
аксиома
железо
ветеран

Sample Output:

машинист
дорога
работа
железо
ветеран
"""


def vow_order(word):
    ind_lst = []
    for i in range(len(word)):
        if word[i] in 'ауоыиэяюёе':
            ind_lst.append(i)
    return ind_lst


match_word = input()
lst_words = [input() for _ in range(int(input()))]

match_lst = []

match_word_ind = vow_order(match_word)

for w in lst_words:
    if vow_order(w) == match_word_ind:
        match_lst.append(w)

print(*match_lst, sep='\n')
