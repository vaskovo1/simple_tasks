
def transform(tpl):
    val = int(tpl[0])
    unit = tpl[1]

    if unit == 'KB':
        val *= 1024
    elif unit == 'MB':
        val *= (1024 * 1024)
    elif unit == 'GB':
        val *= (1024 * 1024 * 1024)

    return val


files = {}
ext_set = set()

with open('files.txt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        line_lst = line.split()

        name = line_lst[0]
        size = tuple(line_lst[1:])
        ext = name.split('.')[1]

        files[name] = [ext, size]
        ext_set.add(ext)


ext_dict = {0: 'B',
            1: 'KB',
            2: 'MB',
            3: 'GB'}

for extension in sorted(ext_set):
    total = 0
    for k,v in sorted(files.items()):
        if extension in v:
            print(f'{k}')
            new_size = transform(v[1])
            total += new_size

    k = 0
    while total > 1024:
        total /= 1024
        k += 1

    print('----------')
    print(f'Summary: {round(total)} {ext_dict[k]}')
    print()

