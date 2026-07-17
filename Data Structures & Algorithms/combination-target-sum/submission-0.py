class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        candidates = []

        def backtracking(i, candidates):
            cur_sum = sum(candidates)
            
            if cur_sum == target:
                output.append(candidates.copy())
                return 
            
            if i >= len(nums) or cur_sum > target:
                return
            
            # left subtree of decision tree
            candidates.append(nums[i])
            backtracking(i, candidates)

            # right subtree
            candidates.pop()
            backtracking(i + 1, candidates)
        
        backtracking(0, candidates)

        return output