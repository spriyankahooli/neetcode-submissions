class LRUCache:

    def __init__(self, capacity: int):
        self.map1 = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:

        if key not in self.map1:
            return -1
        val = self.map1[key]
        self.map1.pop(key)
        self.map1[key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map1:
            self.map1.pop(key)
        elif len(self.map1) == self.capacity:
            del self.map1[next(iter(self.map1))]
        self.map1[key] = value
