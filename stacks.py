'''
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
'''


class PlateStackClass:

    def __init__(self, max_size=3):
        self.elems = []
        self.max_size = max_size

        print(f'The main cmds: add_elem, pop, peek, show_stacks, size, count_all, count_last_stack, info')

    def _add_empty_list(self):
        self.elems.append([])

    def _add_last_elem(self):
        self.elems[-1].append(self.last_value)

    def add_elem(self, value='a plate'):

        self.last_value = value

        if not self.elems:
            self._add_empty_list()
            self._add_last_elem()
        else:
            if len(self.elems[-1]) < self.max_size:
                self._add_last_elem()
            else:
                self._add_empty_list()
                self._add_last_elem()

        self.show_stacks()

    def peek(self):
        if self.elems:
            print(self.elems[-1][-1])
        else:
            print('Empty stack')

    def pop(self):
        self.peek()
        if self.elems:
            if len(self.elems[-1]) == 1:
                del self.elems[-1]
            else:
                self.elems[-1].pop(-1)

        self.show_stacks()

    def show_stacks(self):
        print(self.elems)

    def size(self):
        print(len(self.elems))

    def info(self):
        for i, el in enumerate(self.elems, 1):
            print(str(i) + ' stack has element(s): ', ', '.join(el))

    def count_last_stack(self):
        if self.elems:
            print(len(self.elems[-1]))
        else:
            self.peek()

    def count_all(self):
        if self.elems:
            total = 0
            for el in self.elems:
                total += len(el)
            print(total)
        else:
            self.peek()