from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        vote_counter = defaultdict(int)

        for i in range(len(s)):
            vote_counter[s[i]] += 1
            vote_counter[t[i]] -= 1
        
        for char, freq in vote_counter.items():
            if freq != 0:
                return False
        
        return True