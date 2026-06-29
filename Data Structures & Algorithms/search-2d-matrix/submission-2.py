class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1

        # Run binary search on rows when raws are more than one and find rightmost row
        # whose first element is less than or equal to the target
        if (len(matrix) > 1):
            while start < end:
                mid = start + (end - start) // 2 + 1
                if matrix[mid][0] > target:
                    end = mid - 1
                elif matrix[mid][0] < target:
                    start = mid
                else:
                    return True
        else:
            row = matrix[0]
        
        # Run a simple binary search on this row
        row = matrix[start]
        left, right = 0, len(row) - 1

        while left < right:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return True
            if row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return row[left] == target

        