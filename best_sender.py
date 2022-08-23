"""
Функция best_sender()

Рассмотрим два списка:

messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']

senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

Первый список представляет набор отправленных сообщений в некотором мессенджере,
второй список — набор отправителей этих сообщений. Причем сообщение messages[i]
отправлено пользователем senders[i]. Каждое сообщение представляет собой
последовательность слов, разделенных пробелом (знаки препинания считаются
частями слов). Количество слов — это общее число слов, отправленное
пользователем. Обратите внимание, что каждый пользователь может отправлять
более одного сообщения. Например, пользователь Sam Fisher отправил 2 слова в
первом сообщении и 4 слова во втором, следовательно, его количество слов
равно 2+4=6

Реализуйте функцию best_sender(), которая принимает два аргумента в следующем
порядке:

    messages — список сообщений
    senders — список имен отправителей

Функция должна определять отправителя, имеющего наибольшее количество слов, и
возвращать его имя. Если таких отправителей несколько, следует вернуть имя того,
чье имя больше в лексикографическом сравнении.

Гарантируется, что длины передаваемых в функцию списков совпадают.


Sample Input 1:

messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))

Sample Output 1:

Sam Fisher

Sample Input 2:

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))

Sample Output 2:

Charlie

"""

from collections import defaultdict


def best_sender(messages, senders):
    d = defaultdict(list)
    for i in range(len(senders)):
        d[senders[i]].extend(messages[i].split())

    for k, v in sorted(d.items(), key=lambda x: (-len(x[1]), [-o for o in map(ord, x[0])])):
        return k