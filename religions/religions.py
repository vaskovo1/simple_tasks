import json

relig_stat = {}

with open('countries.json', encoding='utf-8') as file:
    lst = json.load(file)

for d in lst:
    if d['religion'] not in relig_stat:
        relig_stat[d['religion']] = []
        relig_stat[d['religion']].append(d['country'])
    else:
        relig_stat[d['religion']].append(d['country'])

with open('religion.json', 'w', encoding='utf-8') as wf:
    json.dump(relig_stat, wf, indent=3)
