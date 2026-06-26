class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_map = {}

        for i, num in enumerate(nums):
            if num in compliment_map:
                return [compliment_map[num], i]
            compliment_map[target - num] = i
        
        return [-1, -1]