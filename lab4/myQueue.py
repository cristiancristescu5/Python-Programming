class Queue:
    def __init__(self, ls: list):
        if ls is not None:
            self._queue = ls
            self._index = 0
        else:
            self._queue = []
            self._index = 0

    def push(self, el):
        self._queue.append(el)

    def pop(self):
        if len(self._queue) == 0:
            return None
        return self._queue.pop(0)

    def peek(self):
        if len(self._queue) == 0:
            return None
        return self._queue[0]

    def get_queue(self):
        return self._queue
