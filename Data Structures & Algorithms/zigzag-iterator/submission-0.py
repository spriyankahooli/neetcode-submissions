class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors =[v1,v2]
        self.queue = deque()
        for i,v in enumerate(self.vectors):
            if len(v) > 0:
                self.queue.append((i,0))

        

    def next(self) -> int:
        if self.queue:
            v_i,e_i = self.queue.popleft()
            n_ele = e_i+1
            if n_ele < len(self.vectors[v_i]):
                self.queue.append((v_i,n_ele))
            return self.vectors[v_i][e_i]
        return -1

        
        

    def hasNext(self) -> bool:
        return len(self.queue) >0 
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
