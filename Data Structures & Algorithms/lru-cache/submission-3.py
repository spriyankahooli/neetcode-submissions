class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.pop(key)
        self.cache[key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
           self.cache.pop(key) 
        elif len(self.cache) == self.capacity:
            del self.cache[next(iter(self.cache))]
        self.cache[key] = value
        
        
