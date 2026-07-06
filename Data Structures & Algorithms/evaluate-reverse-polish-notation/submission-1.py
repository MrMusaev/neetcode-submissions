class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]
        operands = set(['+', '-', '*', '/'])

        for i in range(1, len(tokens) - 1):
            if tokens[i + 1] in operands:
                firstNum = stack.pop()
                secondNum = int(tokens[i])
                operand = tokens[i + 1]
                if operand == '+':
                    stack.append(firstNum + secondNum)
                elif operand == '-':
                    stack.append(firstNum - secondNum)
                elif operand == '*':
                    stack.append(firstNum * secondNum)
                else:
                    stack.append(firstNum // secondNum)

        return stack.pop()