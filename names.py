"""
Написать функцию преобразующую в словарь словарей,
дальше нужно сделать сортировки внешнего словаря (по фамилиям) и внутреннего по именам.
Сортировка: сначала по фамилиям, потом по именам
"""


data = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
result = {}
finish_result = {}
for person in data:
    name, surname = person.split()
    data_surname = result.setdefault(surname[0], {})
    data_name = data_surname.setdefault(name[0], [])
    data_name.append(person)

for surname in sorted(result):
    finish_result[surname] = {}
    for name in sorted(result[surname]):
        finish_result[surname][name] = result[surname][name]

print(finish_result)