class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            cor_index = abs(num) - 1
            if nums[cor_index] < 0:
                return abs(num)
            nums[cor_index] *= -1
        
        return -1