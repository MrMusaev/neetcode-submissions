import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = collections.Counter(tasks)
        max_heap = [-freq for freq in tasks_count.values()]
        heapq.heapify(max_heap)
        time = 0
        queue = deque() # [[-cnt, idleTime]]
        
        while max_heap or queue:
            time += 1

            if max_heap:
                freq = 1 + heapq.heappop(max_heap)
                if freq:
                    queue.append((freq, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time