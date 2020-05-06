import pdb

class Solution:
    def twoSum(self, nums, target):
        di = {}
        pdb.set_trace()
        for ii, value in enumerate(nums):
            di[value] = ii
            ji = di.get(target-value)
            if ji is not None and ii != ji:
                return [ii, ji]

if __name__ == '__main__':
    obj = Solution()
    a = obj.twoSum([3,3], 6)
    print(a)