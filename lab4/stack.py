class Stack:
    def __init__(self, ls: list):
        if ls is not None:
            self._stack = list(ls)
            self._index = len(ls) - 1
        else:
            self._stack = []
            self._index = -1

    def push(self, el):
        self._index += 1
        self._stack.insert(self._index, el)

    def pop(self):
        if self._index == -1:
            return None

        el = self._stack.pop(self._index)
        self._index -= 1
        # self._stack.remove(el)
        return el

    def peek(self):
        if self._index == -1:
            return None
        return self._stack[self._index]

    def get_index(self):
        return self._index

    def get_stack(self):
        ls = []
        for i in range(self._index + 1):
            ls.append(self._stack[i])
        return ls
