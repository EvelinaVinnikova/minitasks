def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class GlobalCounter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step


gc1 = GlobalCounter(initial_count=10, step=2)
gc2 = GlobalCounter()

assert id(gc1) == id(gc2)
print(gc1.count)
gc1.increment()
print(gc2.count)