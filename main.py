import types


# Задание 1
class FlatIterator:
    """
Итератор, который принимает список списков и возвращает их плоское представление, 
т. е. последовательность, состоящую из вложенных элементов
"""
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.coursor = 0
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.idx < len(self.list_of_lists[self.coursor]):
                item = self.list_of_lists[self.coursor][self.idx]
                self.idx +=1
                return item
            else:
                self.coursor += 1
                self.idx = 0
                return next(self)
        except: 
            raise StopIteration
        
    
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]




# Задание 2
def flat_generator(list_of_lists):
    """Генератор, который принимает список списков и возвращает их плоское представление"""
    for i in list_of_lists:
        for item in i:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


# Задание 3
class FlatIterator:
    """Итератор, аналогичный итератору из задания 1, 
    но обрабатывающий списки с любым уровнем вложенности"""    
    def __init__(self, list_of_lists):
        self.result_element = list(self.rec(list_of_lists))
        self.element = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.element < len(self.result_element):
            item = self.result_element[self.element]
            self.element += 1
            return item
        else:
            raise StopIteration


    def rec(self, elem_list):
        for item in elem_list:
            if isinstance(item, list):
                yield from self.rec(item)
            else:
                yield item
        
 

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']    




# Задание 4
def flat_generator(list_of_list):
    """Генератор, аналогичный генератору из задания 2, 
но обрабатывающий списки с любым уровнем вложенности"""
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item



def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)



if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()