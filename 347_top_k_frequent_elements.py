from typing import List
from queue import PriorityQueue
from collections import Counter
import random

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partiton(unique, count, left, right, p):
    pivot_count = count[unique[p]]

    swap(unique, p, right)

    i = left
    j = left
    while j <= right:
        if count[unique[j]] < pivot_count:
            swap(unique, i, j)
            i = i + 1
        j = j + 1
    swap(unique, right, i)

    return i

def quickselect(unique, count, left, right, k):
    if left == right:
        return

    p_index = random.randint(left, right)

    p_index = partiton(unique, count, left, right, p_index)

    if k == p_index:
        return
    elif k < p_index:
        quickselect(unique, count, left, p_index - 1, k)
    else:
        quickselect(unique, count, p_index + 1, right, k)

class Solution:

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        n = len(unique)
        quickselect(unique, count, 0, n - 1, n - k)
        return unique[n - k:]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        i = 0
        l = len(nums)
        while i < l:
            h[nums[i]] = h.get(nums[i], 0) + 1
            i = i + 1

        queue = PriorityQueue()
        for ch, count in h.items():
            queue.put((-count, ch))

        i = 0
        arr = []
        while i < k:
            item = queue.get()
            arr.append(item[1])
            i = i + 1

        return arr
print(Solution().topKFrequent2([1,1,1,2,2,333333333], 2))
