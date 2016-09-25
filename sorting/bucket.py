"""
MikeMcMahon - 9/24/2016

A bucket sort is VERY similar to a radix sort, in which you break the data into "buckets"
Then for each bucket you perform a sort of choice on said bucket
and then reintegrate all of your buckets
"""
from collections import deque
from random import randrange
from typing import List
from math import ceil

from sorting.radix import radix_sort


def bucket_sort(array: List[int], buckets: int):
    """In place bucket sorting of a list"""
    partition = 0
    for i in array:
        if ceil(i / buckets) > partition:
            partition = ceil(i / buckets)

    queues = [[] for _ in range(buckets)]
    for i in range(len(array)):
        queues[array[i] // partition].append(array[i])

    for q in queues:
        radix_sort(q)

    return [v for q in queues for v in q]


def main():
    rand_nums = [int(randrange(0, 1000)) for _ in range(1000)]
    print(rand_nums)
    rand_nums = bucket_sort(rand_nums, 2)
    print(rand_nums)


if __name__ == "__main__":
    main()
