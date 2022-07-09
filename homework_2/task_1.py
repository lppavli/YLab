import typing


class CyclicIterator:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = max(i for i in stop_value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        else:
            self.current = -1
            self.__next__()
            return self.current


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
