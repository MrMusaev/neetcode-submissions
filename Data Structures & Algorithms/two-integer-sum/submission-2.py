class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}

        for i, n in enumerate(nums):
            difference_map[target - n] = i
        
        for i, n in enumerate(nums):
            if n in difference_map and i != difference_map[n]:
                return [i, difference_map[n]]
        
        return [-1, -1]