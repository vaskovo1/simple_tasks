"""
Программа получает на вход количество файлов n, содержащихся в файловой системе
компьютера. Далее идет n строк, на каждой имя файла и допустимые с ним
операции, разделенные символом пробела. В следующей строке записано число
m — количество запросов к файлам, и затем m строк с запросами вида операция
файл. Одному и тому же файлу может быть адресовано любое количество запросов.

Программа должна вывести для каждого из m запросов в отдельной строке
Access denied или OK.

Для каждого файла известно, с какими действиями можно к нему обращаться:

    запись W (write, доступ на запись в файл);
    чтение R (read, доступ на чтение из файла);
    запуск X (execute, запуск на исполнение файла).


 Sample Input 1:

5
my_pycode.exe W X
log_n X W R
ave R
lucky_m W R
dnsss.py W
6
execute ave
read dnsss.py
write log_n
execute log_n
read ave
write my_pycode.exe

Sample Output 1:

Access denied
Access denied
OK
OK
OK
OK


 Sample Input 2:

2
marvel_movies X
dc_com X R
2
execute dc_com
write dc_com

Sample Output 2:

OK
Access denied
"""

files_dct, cmd_lst = {}, []

for _ in range(int(input())):
    file, *permission = input().split()
    files_dct[file] = permission

for _ in range(int(input())):
    cmd_lst.append(tuple(input().split()))

cmd_cod = {'execute': 'X',
           'read': 'R',
           'write': 'W'}

for command in cmd_lst:
    if cmd_cod[command[0]] in files_dct[command[1]]:
        print('OK')
    else:
        print('Access denied')