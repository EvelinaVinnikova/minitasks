def specialize(f, *args, **kwargs):
    def specialized_function(*more_args, **more_kwargs):
        all_args = args + more_args
        all_kwargs = {**kwargs, **more_kwargs}
        return f(*all_args, **all_kwargs)
    return specialized_function

def sum(x, y):
    return x + y

def mult(x, y, z):
    return x * y * z

def greet(name, title):
    return f"Hello {title} {name}"


plus_one = specialize(sum, y = 1)
assert plus_one(10) == 11

just_two = specialize(sum, "abc", "kgf")
assert just_two() == "abckgf"

multiply_three = specialize(mult, -1, 6, 0.9)
assert multiply_three() == -5.4

no_spezialization = specialize(sum)
assert no_spezialization(3, 4) == 7

greet_dr = specialize(greet, title="Dr.")
assert greet_dr("Smith") == "Hello Dr. Smith", "greet_dr('Smith') should return 'Hello Dr. Smith'"

