class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity  # max_size cache
        self.cache = {}
        self.order = []  # array of keys

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                oldest_key = self.order.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = value
            self.order.append(key)

cache = LRUCache(3)
cache.put(1, "one")
cache.put(2, "two")
cache.put(3, "three")

b = (cache.get(1))  # ключ 1 используется
cache.put(4, "four")  # Кэш заполнен, значит удаляем самый старый ключ - 2
a = cache.get(2)
assert a == None, print("Assert error\n")
a = cache.get(3)
assert a == "three", print("Assert error\n")
a = cache.get(4)
assert a == "four", print("Assert error\n")