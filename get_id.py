"""
В онлайн-школе BEEGEEK имя ученика считается корректным, если оно начинается с
заглавной латинской буквы, за которой следуют строчные латинские буквы.
Например, имена Timur и Yo считаются корректными, а имена timyrik, Yo17,
TimuRRR нет. Также у каждого ученика имеется идентификационный номер,
представленный натуральным числом, который выдается при поступлении в школу. К
примеру, если в школе обучается 10 учеников, то новый прибывший ученик
получит идентификационный номер равный 11.

Реализуйте функцию get_id(), которая принимает два аргумента:

    names — список имен учеников, обучающихся в школе
    name — имя поступающего ученика

Функция должна возвращать идентификационный номер, который получит поступающий
в школу ученик, при этом

    если имя ученика name не является строкой (тип str), функция должна
    возбуждать исключение:

    TypeError('Имя не является строкой')

    если имя ученика name является строкой (тип str), но не представляет собой
    корректное имя, функция должна возбуждать исключение:

    ValueError('Имя не является корректным')




Sample Input 1:

names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))

Sample Output 1:

4

Sample Input 2:

names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

Sample Output 2:

Имя не является корректным

Sample Input 3:

names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

Sample Output 3:

Имя не является строкой

"""


def get_id(names, name):
    if type(name) is not str:
        raise TypeError('Имя не является строкой')
    if not name.isalpha() or name != name.title():
        raise ValueError('Имя не является корректным')
    return len(names) + 1


