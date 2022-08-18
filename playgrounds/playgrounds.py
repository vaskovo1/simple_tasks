import json, csv

with open('playgrounds.csv', encoding='utf-8') as f, open('addresses.json', 'w', encoding='utf-8') as wf:
    rows = csv.reader(f, delimiter=';')
    dct = {}
    for row in rows:
        break
    for row in rows:

        admarea = row[1]
        district = row[2]
        address = row[3]

        if admarea not in dct:
            dct[admarea] = {}

        if district not in dct[admarea]:
            dct[admarea][district] = []

        dct[admarea][district].append(address)

    json.dump(dct, wf, indent=3, ensure_ascii=False)
