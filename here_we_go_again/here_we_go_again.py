from collections import Counter
from csv import reader

c = Counter()
with open('name_log.csv', encoding='utf-8') as f:
    it = reader(f)
    for rec in it:
        break
    for rec in it:
        c.update([rec[1]])

    for k, v in sorted(c.items()):
        print(f'{k}: {v}')