class Solution:
    def calculate(self, s: str) -> int:
        stack =[]
        num =0
        operator ='+'
        for i,ch in enumerate(s):
            if ch.isdigit():
                num = num*10+int(ch)
            if ch in '+-*/' or i ==len(s)-1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop()*num )
                elif operator =='/':
                    stack.append(int(stack.pop()/num))
                operator =ch
                num=0
        return sum(stack)
        