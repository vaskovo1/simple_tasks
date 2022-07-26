def choose_plural(num, tpl):
    end = int(str(num)[-1])
    if len(str(num)) >= 2:
        if int(str(num)[-2]) == 1:
            ind = 2
        else:
            ind = auxiliary(end)
    else:
        ind = auxiliary(end)
    return f'{str(num)} {tpl[ind]}'


def auxiliary(number):
    if number == 1:
        ind = 0
    elif 2 <= number <= 4:
        ind = 1
    elif number == 0 or number > 4:
        ind = 2
    return ind


print(choose_plural(1012, ('яблоко', 'яблока', 'яблок')))  # 1012 яблок
print(choose_plural(21, ('пример', 'примера', 'примеров')))  # 21 пример
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))  # 92 гвоздя
print(choose_plural(1, ('яблоко', 'яблока', 'яблок')))  # 1 яблоко
print(choose_plural(102, ('пример', 'примера', 'примеров')))  # 102 примера
print(choose_plural(2025, ('гвоздь', 'гвоздя', 'гвоздей')))  # 2025 гвоздей
