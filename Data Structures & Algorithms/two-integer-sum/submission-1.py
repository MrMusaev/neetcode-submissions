class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}

        for i in range(len(nums)):
            difference_map[target - nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in difference_map.keys():
                return [i, difference_map[nums[i]]]
        
        return [-1, -1]