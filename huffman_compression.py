from collections import defaultdict
from heapq import heapify, heappop, heappush
from queue import PriorityQueue
from typing import List, Tuple, Iterable

from datastructures.binarytree import Tree, TreeLeaf


def huffman_sort(raw_items: Iterable[Tuple[any, any]]) -> List[Tuple[any, any]]:
    # important that we put the number first, and the letter second
    return sorted([(p, d) for d, p in raw_items], key=lambda p: "{}{}".format(p[0], p[1]))


def main():
    input_word = "helloworldhowareyou".upper()

    # get the frequency of each character and build it into a dict
    symbol_frequency = defaultdict(int)
    for ch in input_word:
        symbol_frequency[ch] += 1

    huffman_table = huffman_sort(symbol_frequency.items())

    # The basic algo is to grab the smallest two (our first two)
    # they make a node, or are the basis of a node and new node
    huffman_bst = gen_huffman_tree(huffman_table)
    #huffman = encode(symbol_frequency)
    #return huffman


def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def gen_huffman_tree(table):
    p_queue = PriorityQueue()
    nodes = [(x[0], TreeLeaf(x[0], x[1])) for x in table]
    heapify(nodes)

    for node in nodes:
        p_queue.put(node)

    while not p_queue.empty() and p_queue.qsize() > 1:
        left, right = p_queue.get(False), p_queue.get(False)
        p_queue.task_done()
        p_queue.task_done()
        new_node = TreeLeaf(left[0] + right[0])
        new_node.left = left[1]
        new_node.right = right[1]

        p_queue.put_nowait((new_node.weight, new_node))
    weight, node = p_queue.get(False)
    return


def get_node_value(data: any):
    if type(data) is tuple:
        return data[0]
    return data.weight

    #
    #
    # while table:
    #     if 2 > len(table):
    #         left = table[-1]
    #         table.pop()
    #         bst_raw.append(left)
    #         continue
    #
    #     right, left = table[-2:]
    #     table.pop()
    #     table.pop()
    #
    #     leaf = TreeLeaf(right[1] + left[1])
    #     leaf.left = TreeLeaf(left[0])
    #     leaf.right = TreeLeaf(right[0])
    #
    #     table.append((index, right[1] + left[1], leaf))
    #     table = huffman_sort(table)
    #     index += 1
    #
    #     bst_raw.append((left, right))
    #
    # bst_raw = [(get_bst_value(x), get_bst_value(y)) for x, y in bst_raw[:-1]] + [bst_raw[-1][1]]
    # for bst in bst_raw:
    #     print(bst)
    # return generate_table(bst_raw)


def get_bst_value(data):
    # If the value is a character we want it, otherwise it's just another branch
    return data[0] if type(data[0]) is str else data[1]


def generate_table(bst_raw) -> Tree:
    bst = Tree()
    bst.add(bst_raw[-1])  # add the root of the tree
    bst_raw.pop()

    while bst_raw:
        d1, d2 = bst_raw.pop()
        if type(d1) is int:  # we have an frequency not a value
            pass

if __name__ == "__main__":
    main()