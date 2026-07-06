class Solution:
    def findTwoSum(self, nums, left, target):
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [nums[left], nums[right]]
            if sum < target:
                left += 1
            else:
                right -= 1
        return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            num = nums[i]
            two_pairs = self.findTwoSum(nums, i + 1, -num)
            if len(two_pairs) > 0:
                result.append([num, two_pairs[0], two_pairs[1]])
        
        return result