class Solution:        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []

        def backtrack(i: int) -> None:
            if i == len(nums):
                output.append(subset.copy())
                return 
            
            # include nums[i], left branch of decision tree
            subset.append(nums[i])
            backtrack(i + 1)

            # exclude nums[i], right branch of decision tree
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return output