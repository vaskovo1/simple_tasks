from datetime import datetime

dct = {}

with open('diary.txt', encoding='UTF-8') as file:
    for line in file:
        line = line.strip()
        if ':' in line:
            t = datetime.strptime(line, '%d.%m.%Y; %H:%M')
            dct[t] = []
            continue
        if line != '':
            dct[t].append(line)

for d in sorted(dct):
    print(d.strftime('%d.%m.%Y; %H:%M'))
    for el in dct[d]:
        print(el)
    print()
