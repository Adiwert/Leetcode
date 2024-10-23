class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for id1 in range(len(nums)):
            for id2 in range(id1 + 1, len(nums)):
                if nums[id1] + nums[id2] == target:
                    return [id1, id2]