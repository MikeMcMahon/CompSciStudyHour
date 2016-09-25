"""
MikeMcMahon - 9/24/2016

The radix sort is a nifty sorting algorithm that divides/conquers the sorting by breaking
integers into buckets based on their digit place

Best Case is
worst Case is O(wn) for performance
worst Case is O(w * N) for space
"""
from collections import deque
from typing import List


def radix_sort(array: List[int]) -> List[int]:
    queues = [deque() for _ in range(10)]

    # Starting at the number place
    digit = 1

    processing = True
    while processing:
        processing = False
        for i in range(len(array)):
            d_value = int(array[i] / digit) % 10
            queues[d_value].append(array[i])
            array[i] -= d_value

            # If the digit we're checking is less than the max size of some indeterminate number
            # Then we need to continue processing, otherwise this will be the final iteration
            if digit < array[i]:
                processing = True
        a = 0
        for q in queues:
            while len(q) > 0:
                array[a] = q.popleft()
                a += 1

        digit *= 10


def main():
    to_be_sorted = [30, 22, 400, 231, 11, 32, 4, 1, 9, 78, 300]
    radix_sort(to_be_sorted)

    to_be_sorted2 = [140, 100, 110, 120, 130]
    radix_sort(to_be_sorted2)

    print(to_be_sorted)
    print(to_be_sorted2)


if __name__ == "__main__":
    main()