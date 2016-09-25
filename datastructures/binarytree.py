from typing import Tuple


class TreeLeaf(object):
    def __init__(self, weight: int, data: any=None):
        self.left = None
        self.right = None
        self.weight = weight
        self.data = data

    def __str__(self):
        return self.data
        #"{} {}".format(self.data if self.data else "_", self.weight)

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, data: any) -> None:
        if not self.root:
            self.root = TreeLeaf(data)
        else:
            self.__add(data, self.root)

    def __add(self, data, leaf):
        if data < leaf.data:
            if leaf.left is not None:
                self.__add(data, leaf.left)
            else:
                leaf.left = TreeLeaf(leaf)
        else:
            if leaf.right is not None:
                self.__add(data, leaf.right)
            else:
                leaf.right = TreeLeaf(data)

