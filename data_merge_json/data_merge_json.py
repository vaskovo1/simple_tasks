import json

with open('data1.json', encoding='utf-8') as file1, open('data2.json', encoding='utf-8') as file2, open('data_merge.json', 'w', encoding='utf-8') as file3:
    data1 = json.load(file1)
    data2 = json.load(file2)
    data1.update(data2)
    json.dump(data1, file3, indent=3)