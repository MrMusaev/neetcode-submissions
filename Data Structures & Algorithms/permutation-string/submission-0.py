class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1, ls2 = len(s1), len(s2)
 
        if ls2 < ls1:
            return False
        
        # Create a counter of s1 using an array
        counterS1 = [0] * 26
        for ch in s1:
            index = ord(ch) - ord('a')
            counterS1[index] += 1
        
        # Init counter for substring and sliding window
        counterSub = [0] * 26
        left, right = 0, 0
        
        while right < ls2:
            indexR = ord(s2[right]) - ord('a')            
            counterSub[indexR] += 1

            if right - left + 1 == ls1:
                if counterSub == counterS1:
                    return True
                indexL = ord(s2[left]) - ord('a')
                counterSub[indexL] -= 1
                left += 1
            
            right += 1
        
        return False
            