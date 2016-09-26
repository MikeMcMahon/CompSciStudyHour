"""
Mike McMahon
"""
from typing import List


class LinkedList(object):

    class Node(object):

        def __init__(self, data: any = None, next_node=None):
            self._data = data
            self._next = next_node

        def get_next(self):
            return self._next

        def set_next(self, next_node):
            self._next = next_node

        def set_data(self, data):
            self._data = data

        def __str__(self):
            return str(self._data)

    def __init__(self, initial: List=None):
        self._size = len(initial) if initial else 0
        self._root = None
        self._tail = None

        if initial:
            for i in range(len(initial)):
                if i == 0:
                    self._root = LinkedList.Node(initial[i])
                    self._tail = self._root
                else:
                    self._tail.set_next(LinkedList.Node(initial[i]))
                    self._tail = self._tail.get_next()

    def add(self, value):
        self._tail.set_next(LinkedList.Node(value))
        self._tail = self._tail.get_next()
        self._size += 1

    def __len__(self):
        return self._size

    def remove(self, i=None):
        """
        Removes the element at a given position, if no position specified this will grab the tail (always O(1))
        :param i:
        :return:
        """

        if i:
            if i > self._size:
                raise IndexError

            if i == 0:
                self._root = self._root.get_next()

            prev = None
            to_remove = self._root
            for i in range(0, i):
                prev = to_remove
                to_remove = to_remove.get_next()

            prev.set_next(prev.get_next().get_next())
            self._size -= 1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    llist = LinkedList(arr)
    print(len(llist))
    llist.remove(3)
    print(len(llist))

if __name__ == "__main__":
    main()
