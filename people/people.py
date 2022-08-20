import json

with open('people.json', encoding='utf-8') as f:
    p = json.load(f)

myset = set()

for d in p:
    for k in d:
        myset.add(k)

for key in myset:
    for dct in p:
        if key not in dct:
            dct[key] = None

with open('updated_people.json', 'w', encoding='utf-8') as wf:
    json.dump(p, wf, indent=3)