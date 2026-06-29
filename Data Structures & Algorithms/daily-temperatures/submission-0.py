class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer_candidates = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while warmer_candidates and temperatures[warmer_candidates[-1]] <= temperatures[i]:
                warmer_candidates.pop()
            
            if warmer_candidates:
                result[i] = warmer_candidates[-1] - i
            
            warmer_candidates.append(i)
        
        return result