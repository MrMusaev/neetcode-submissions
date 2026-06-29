class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(['+', '-', '*', '/'])

        for i in range(len(tokens)):
            if tokens[i] not in operands:
                stack.append(int(tokens[i]))
            else:
                secondNum = stack.pop()
                firstNum = stack.pop()
                operand = tokens[i]
                if operand == '+':
                    stack.append(firstNum + secondNum)
                elif operand == '-':
                    stack.append(firstNum - secondNum)
                elif operand == '*':
                    stack.append(firstNum * secondNum)
                else:
                    stack.append(int(firstNum / secondNum))

        return stack.pop()