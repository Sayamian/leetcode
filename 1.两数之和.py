1. 暴力解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

2. 两次哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {value: index for index, value in enumerate(nums)}
        for i, value in enumerate(nums):
            j = d.get(target-value)
            if j and i != j:
                return [i, j]

3. 一次哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, value in enumerate(nums):
            j = d.get(target-value)
            if j is not None and i != j:
                return sorted([i,j])
            d[value] = i