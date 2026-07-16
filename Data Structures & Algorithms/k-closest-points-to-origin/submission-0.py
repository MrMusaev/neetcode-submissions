class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            distance = math.sqrt(point[0] * point[0] + point[1] * point[1])
            heapq.heappush(maxHeap, (-distance, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
                
        return [point[1] for point in maxHeap]