class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)

        for num, freq in counter.items():
            if freq > n // 2:
                return num