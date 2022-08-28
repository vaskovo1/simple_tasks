from json import load
from csv import writer

with open('students.json', encoding='utf-8') as f, open('data.csv', 'w', encoding='utf-8', newline='') as wf:
    wr = writer(wf, delimiter=',')
    wr.writerow(['name', 'phone'])
    students = load(f)
    for student in sorted(students, key= lambda x: x['name']):
        if student['age'] >= 18 and student['progress'] >= 75:
            wr.writerow([student['name'], student['phone']])