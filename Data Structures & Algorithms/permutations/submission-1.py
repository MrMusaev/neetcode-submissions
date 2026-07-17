class Solution:
    def backtrack(self, nums: List[int], output: List[List[int]], candidate: List[int], used: set):
        if len(candidate) == len(nums):
            output.append(candidate.copy())
            return
        
        for num in nums:
            if num in used:
                continue
            
            # Add num to candidate list and used set
            candidate.append(num)
            used.add(num)

            # Recursively explore other branches using updated candidate
            self.backtrack(nums, output, candidate, used)

            # Clean up the candidate for backtracking
            candidate.pop()
            used.remove(num)

    def permute(self, nums: List[int]) -> List[List[int]]:
        output, candidate = [], []
        self.backtrack(nums, output, candidate, set())
        return output