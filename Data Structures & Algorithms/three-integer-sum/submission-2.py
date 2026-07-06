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
            pairs = self.findTwoSum(nums, i + 1, -num)

            if len(pairs) == 0:
                continue

            triples = [num, pairs[0], pairs[1]]
            if len(result) > 0 and result[-1] == triples:
                continue
            
            result.append(triples)
        
        return result