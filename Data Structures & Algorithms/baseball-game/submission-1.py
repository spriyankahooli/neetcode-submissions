class Solution:
    def calPoints(self, operations: List[str]) -> int:
            result = 0
            stack = []
            for op in operations:
                if op == 'C':
                    stack.pop()
                elif op == 'D':
                    a = (stack[-1]*2)
                    stack.append(a)
                elif op == '+':
                    stack.append(stack[-2]+stack[-1])
                else:
                    stack.append(int(op))
            result = sum(stack)
            return result
                    

       
        