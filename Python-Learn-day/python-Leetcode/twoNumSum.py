class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}
        for i, num in enumerate(nums):
            if target - num in dict1:
                return [dict1[target - num], i]
            dict1[num] = i
        return []


