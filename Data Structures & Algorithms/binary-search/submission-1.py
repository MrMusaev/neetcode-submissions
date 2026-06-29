class Solution:
    def binSearchRec(self, nums, target, left, right):
        if left > right:
            return -1
        
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binSearchRec(nums, target, mid + 1, right)
        else:
            return self.binSearchRec(nums, target, left, mid - 1)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearchRec(nums, target, 0, len(nums) - 1)