from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [0 for x in range(2 * n)]
        i = 0
        while i < n:
            arr[i * 2] = nums[i]
            arr[i * 2 + 1] = nums[n + i]
            i = i + 1
        return arr
        

Solution().shuffle([1,2,3,4,4,3,2,1], 4)
