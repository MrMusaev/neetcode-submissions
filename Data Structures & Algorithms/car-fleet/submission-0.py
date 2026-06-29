class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)
        for i in range(n):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)
        stack = []
        
        for i in range(n):
            positionI, speedI = cars[i]
            timeI = (target - positionI) / speedI
            if stack and stack[-1] >= timeI:
                continue
            stack.append(timeI)

        return len(stack)