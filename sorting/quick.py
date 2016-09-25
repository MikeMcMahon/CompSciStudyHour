"""
MikeMcMahon - 9/25/2016
"""
from random import randrange
from typing import List


def qsort(array: List[int]):
    """
    Quick sort with a fat partition to avoid duplicate values
    :param array:
    :param lo:
    :param hi:
    :return:
    """

    if len(array) <= 1:
        return array

    lo = []
    # By using a fat partition / pivot we are solving the dutch flag problem of sorting multiple of the same value
    pivots = []
    hi = []

    # Random pivot, but if we wanted to we could select the median of the values
    pivot = array[randrange(0, len(array) - 1)]

    for i in array:
        if i < pivot:
            lo.append(i)
        elif i > pivot:
            hi.append(i)
        else:
            pivots.append(i)

    # Prevents useless qsorts (extra stack frame that simply returns) when
    # all values match the pivot as would happen in the dutch flag problem
    if lo:
        lo = qsort(lo)
    if hi:
        hi = qsort(hi)

    return lo + pivots + hi


def main():
    a = [randrange(0, 50) for _ in range(100)]
    print(a)
    a = qsort(a)
    print(a)


if __name__ == "__main__":
    main()
