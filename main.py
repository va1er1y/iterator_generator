# 1. Написать итератор, который принимает список списков, и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.

class FlatIterator():
    def __init__(self, collection):
        self.collection = collection


    def __iter__(self):
        self.cursor = -1
        self.results = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.results)
        except StopIteration:
            self.cursor += 1
            if self.cursor == len(self.collection):
                raise StopIteration()
            results = self.collection[self.cursor]
            self.results = iter(results)
            item = next(self.results)
        return (item)

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

for item in FlatIterator(nested_list):
    print(item)
print()

# 2.Написать генератор, который принимает список списков, и возвращает их плоское представление.

def flat_generator(list):
    zip = []
    for i in list:
        zip.extend(i)
    yield (str(zip).strip('[]'))

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
print()

#3. Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности

class FlatIterator():

    def __init__(self, collection):
        self.collection = collection
        self.cursor = -1

    def flatten(self, s):
        if s == []:
            return s
        if isinstance(s[0], list):
            return (self.flatten(s[0]) + self.flatten(s[1:]))
        return (s[:1] + self.flatten(s[1:]))

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.flatten(self.collection)):
            raise StopIteration()
        return (self.flatten(self.collection)[self.cursor])


nested_list = [
    [['a', 'b', 'c'],
    [ [1, 2, None]], [[[12,90]]]]
]

for item in FlatIterator(nested_list):
    print(item)
print()

# 4 Написать генератор аналогичный генератор из задания 2, но обрабатывающий списки с любым уровнем вложенности
def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return(flatten(s[0]) + flatten(s[1:]))
    return(s[:1] + flatten(s[1:]))

def flat_generator(list):
    yield flatten(list)

for item in flat_generator(nested_list):
    print(item)
