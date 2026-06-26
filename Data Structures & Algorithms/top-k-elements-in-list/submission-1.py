class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        counter_tuples = []

        for num, freq in counter.items():
            counter_tuples.append((freq, num))
        
        counter_tuples.sort(reverse=True)

        result = []
        for i in range(k):
            if i < len(counter_tuples):
                result.append(counter_tuples[i][1])
        
        return result