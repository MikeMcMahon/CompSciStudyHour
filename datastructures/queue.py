"""
MikeMcMahon - 9/26/2016
"""


class MyQueue(object):
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, data):
        self._queue.append(data)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)
        else:
            raise Exception("No elements found in queue")

    def empty(self):
        return not bool(self._queue)

    def next(self):
        if self.empty():
            raise StopIteration
        else:
            return self.dequeue()
