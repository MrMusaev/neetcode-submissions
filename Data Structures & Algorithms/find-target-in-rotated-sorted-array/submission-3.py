class Solution:
      def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Check if we found the target in mid 
            # if not then we can eliminate it from further checks
            if nums[mid] == target:
                return mid
            
            # Check if left subarray is sorted
            if nums[left] <= nums[mid]:
                # Check if the target is within this half and drop right chunk if so
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Otherwise drop this chunk (left)
                else:
                    left = mid + 1
            # Right subarray is sorted
            else:
                # Check if the target is within this half and drop left chunk if so
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Otherwise drop this chunk (right)
                else:
                    right = mid - 1

        # Target not found
        return -1