class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = {
            '(': ')', 
            '[': ']', 
            '{': '}',
        }

        for bracket in s:
            if bracket in openings:
                stack.append(bracket)
                continue
            
            if len(stack) == 0:
                return False
                
            opening_b = stack.pop()
            if openings[opening_b] != bracket:
                return False
    
        return len(stack) == 0