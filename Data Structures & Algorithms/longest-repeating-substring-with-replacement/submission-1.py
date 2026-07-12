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

            if numOfCharToReplace > k:
                charFreq[s[left]] -= 1
                left += 1

            right += 1

        return right - left