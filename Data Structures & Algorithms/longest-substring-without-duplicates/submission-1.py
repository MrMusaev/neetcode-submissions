class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()
        lLongestSub = 0
        left, right = 0, 0
        n = len(s)

        while right < n:
            if s[right] in subSet:
                lLongestSub = max(len(subSet), lLongestSub)
                # shrink the window from the left until we remove the found item from set
                while s[right] in subSet and left <= right:
                    subSet.remove(s[left])
                    left += 1
                
            subSet.add(s[right])
            right += 1
        
        return max(len(subSet), lLongestSub)