from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)
        highestFreq = 0
        left = right = 0
        n = len(s)

        while right < n:
            charFreq[s[right]] += 1
            highestFreq = max(highestFreq, charFreq[s[right]])
            windowL = right - left + 1
            numOfCharToReplace = windowL - highestFreq

            # slide the window when condition is NOT met
            if numOfCharToReplace > k:
                charFreq[s[left]] -= 1
                left += 1

            # expands window when condition is met 
            # and slides when it is not met
            right += 1

        # as window does not shrink, the final size - 1 is the answer
        return right - left