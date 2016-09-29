"""

 - 9/28/2016

"""
from random import randrange
from typing import List


def bsort(array: List[int]):
    modified = False

    size = len(array) - 1
    for i in range(size):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            modified = True

        i += 1
    if modified:
        bsort(array)


def main():
    to_sort = [randrange(0, 50) for _ in range(50, 0, -1)]
    print(to_sort)
    bsort(to_sort)
    print(to_sort)
    return 0


if __name__ == "__main__":
    main()
