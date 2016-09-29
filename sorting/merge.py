"""

 - 9/28/2016

"""
from random import randrange
from typing import List


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def merge(left, right) -> List:
    l_idx, r_idx = 0, 0
    results = []
    while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] <= right[r_idx]:
                results.append(left[l_idx])
                l_idx += 1
            else:
                results.append(right[r_idx])
                r_idx += 1

    # Copy the remaining values into the array to be sorted on another recursion
    if l_idx < len(left):
        results.extend(left[l_idx:])
    if r_idx < len(right):
        results.extend(right[r_idx:])

    return results


def main():
    to_sort = [randrange(0, 50) for _ in range(50)]
    print(to_sort)
    to_sort = merge_sort(to_sort)
    print(to_sort)
    return


if __name__ == "__main__":
    main()
