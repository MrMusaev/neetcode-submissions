class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(': ')', 
            '[': ']', 
            '{': '}',
        }

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
                continue
            
            if len(stack) == 0:
                return False

            opening_b = stack.pop()
            if brackets[opening_b] != bracket:
                return False
    
        return len(stack) == 0