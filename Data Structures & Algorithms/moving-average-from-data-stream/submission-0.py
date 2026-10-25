class MovingAverage:

    def __init__(self, size: int):
        self.size = size 
        self.lists = deque()
        

    def next(self, val: int) -> float:
        if len(self.lists) == self.size:
            self.lists.popleft()
        self.lists.append(val)
        avg = sum(self.lists) / len(self.lists)
        return avg