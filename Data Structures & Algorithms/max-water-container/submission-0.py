class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_size = 0

        while left < right:
            c_size = min(heights[left], heights[right]) * (right - left)
            max_size = max(c_size, max_size)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return max_size