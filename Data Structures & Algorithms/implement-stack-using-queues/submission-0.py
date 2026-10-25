class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack = [x]+self.stack
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        val = self.stack.pop(0)
        return val

        
    def top(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        if not self.stack:
            return True 
        else:
            return False 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()