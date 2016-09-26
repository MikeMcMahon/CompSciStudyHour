"""
MikeMcMahon - 9/24/2016

A heap is a kind of binary tree in which elements are stored from max-down or
min-down for any given node it's children may be located at its index * 2 (0) and (index * 2) + 1 (1)

We have prefixed our heaps with a [0] element to simplify the math required for locating children. Is this a good
tradoff? Likely not, but in python it is absurdly easy and probably considered a slight abuse of the language, but
damn...it looks good
"""


class MinHeap:
    def __init__(self):
        # The default zero is not used, but prevents us from having to deal with
        # integer division later on..
        self.heap = [0]
        self.heap_size = 0

    def _sift_up(self, index):
        while index // 2 > 0:
            if self.heap[index] < self.heap[index // 2]:
                self.heap[index // 2], self.heap[index] = self.heap[index], self.heap[index // 2]

            index //= 2

    def min_child(self, index):
        if (index * 2) + 1 > self.heap_size:
            return index * 2
        else:
            if self.heap[index * 2] < self.heap[(index * 2) + 1]:
                return index * 2
            else:
                return (index * 2) + 1

    def _sift_down(self, index):
        while (index * 2) <= self.heap_size:
            min_child = self.min_child(index)
            if self.heap[index] > self.heap[min_child]:
                self.heap[index], self.heap[min_child] = self.heap[min_child], self.heap[index]
            index = min_child

    def delete(self):
        rval = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap_size -= 1
        self.heap.pop()
        self._sift_down(1)
        return rval

    def insert(self, value):
        self.heap.append(value)
        self.heap_size += 1
        self._sift_up(self.heap_size - 1)

    def heapify(self, values):
        i = len(values) // 2
        self.heap_size = len(values)
        self.heap = [0] + values[:]
        while i > 0:
            self._sift_down(i)
            i -= 1


class MaxHeap:
    def __init__(self):
        # The default zero is not used, but prevents us from having to deal with
        # integer division later on..
        self.heap = [0]
        self.heap_size = 0

    def _sift_up(self, index):
        while index // 2 > 0:
            if self.heap[index] > self.heap[index // 2]:
                self.heap[index // 2], self.heap[index] = self.heap[index], self.heap[index // 2]

            index //= 2

    def max_child(self, index):
        if (index * 2) + 1 > self.heap_size:
            return index * 2
        else:
            if self.heap[index * 2] > self.heap[(index * 2) + 1]:
                return index * 2
            else:
                return (index * 2) + 1

    def _sift_down(self, index):
        while (index * 2) <= self.heap_size:
            mc = self.max_child(index)
            if self.heap[index] < self.heap[mc]:
                self.heap[index], self.heap[mc] = self.heap[mc], self.heap[index]
            index = mc

    def delete(self):
        rval = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap_size -= 1
        self.heap.pop()
        self._sift_down(1)
        return rval

    def insert(self, value):
        self.heap.append(value)
        self.heap_size += 1
        self._sift_up(self.heap_size - 1)

    def heapify(self, values):
        i = len(values) // 2
        self.heap_size = len(values)
        self.heap = [0] + values[:]
        while i > 0:
            self._sift_down(i)
            i -= 1


def main():
    raw_heap = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    heap = MinHeap()

    for i in raw_heap:
        heap.insert(i)  # O(n log n) time complexity with siftUp

    heap2 = MinHeap()
    heap2.heapify(raw_heap)  # O(n) complexity with siftDown

    heap3 = MaxHeap()

    for i in raw_heap:
        heap3.insert(i)

    heap3.heapify(raw_heap)

    return heap


if __name__ == "__main__":
    main()
