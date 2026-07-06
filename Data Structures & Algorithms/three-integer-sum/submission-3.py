class Solution:
    def findTwoSums(self, nums, left, target):
        right = len(nums) - 1
        two_pairs = []
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                two_pairs.append([nums[left], nums[right]])
            if sum < target:
                left += 1
            else:
                right -= 1

        return two_pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            num = nums[i]
            pairs_list = self.findTwoSums(nums, i + 1, -num)

            if len(pairs_list) == 0:
                continue

            for pairs in pairs_list:
                triples = [num, pairs[0], pairs[1]]
                if len(result) > 0 and result[-1] == triples:
                    continue
                
                result.append(triples)
        
        return result