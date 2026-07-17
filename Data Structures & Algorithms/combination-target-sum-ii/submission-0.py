class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        combinations = []
        candidates.sort()

        def backtracking(i, combinations, cur_sum):   
            if cur_sum == target:
                output.append(combinations.copy())
                return 

            if i >= len(candidates) or cur_sum > target:
                return
            
            combinations.append(candidates[i])
            backtracking(i + 1, combinations, cur_sum + candidates[i])

            combinations.pop()
            # Skip duplicate elements
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtracking(i + 1, combinations, cur_sum)
            
        backtracking(0, combinations, 0)
        return output