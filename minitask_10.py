def singleton(cls):
    instance = None
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self._cls = cls

        def __call__(self, *args, **kwargs):
            nonlocal instance
            if instance is None:
                instance = self._cls(*args, **kwargs)
            return instance

        def __getattr__(self, name):
            return getattr(self._cls, name)
    return Wrapper()

@singleton
class GlobalCounter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step

@singleton
class Test:
    some_global_field = 123


# Testing
print(Test.some_global_field)
gc1 = GlobalCounter(initial_count=10, step=2)
gc2 = GlobalCounter()

assert id(gc1) == id(gc2)

print(gc1.count)
gc1.increment()
print(gc2.count)
