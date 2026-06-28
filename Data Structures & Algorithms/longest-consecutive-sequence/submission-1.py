class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            # num already counted
            if num - 1 in nums_set:
                continue
            
            # start of a new seq
            current_seq = 1
            while num + 1 in nums_set:
                current_seq += 1
                num += 1
            longest_seq = max(current_seq, longest_seq)

        return longest_seq