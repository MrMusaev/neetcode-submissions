class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minE = float('inf')

        if len(self.stack) > 0:
            currentMin = self.stack[-1][1]
            minE = min(currentMin, val)
        else:
            minE = val
        
        self.stack.append((val, minE))

    def pop(self) -> None:
        if len(self.stack) <= 0:
            return 
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) <= 0:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) <= 0:
            return None
        return self.stack[-1][1]
