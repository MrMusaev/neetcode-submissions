from collections import defaultdict

class Solution:
    def isSubset(self, freqS, freqT):
        for ch, freq in freqT.items():
            if ch not in freqS:
                return False
            
            if freqS[ch] < freqT[ch]:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        # edge case 
        if len(t) > len(s):
            return ""
        
        # create char freq for t
        freqT = defaultdict(int)
        for ch in t:
            freqT[ch] += 1
        
        left, right = 0, 0
        freqS = defaultdict(int)
        found = False
        result = s
        candidate = ""

        while right < len(s):
            freqS[s[right]] += 1

            while self.isSubset(freqS, freqT):
                candidate = s[left:right+1]
                result = candidate if len(candidate) < len(result) else result
                freqS[s[left]] -= 1
                left += 1
                found = True

            right += 1
        
        return result if found else ""
