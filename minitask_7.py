import functools

def deprecated(func=None, *, since=None, will_be_removed=None):
    if func is None:
        return lambda f: deprecated(f, since=since, will_be_removed=will_be_removed)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        prefix = f"Warning: function {func.__name__} is deprecated"
        main_message = f"."
        postfix = f" It will be removed in future versions."
        if since:
            main_message = f" since version {since}."
        if will_be_removed:
            postfix = f" It will be removed in version {will_be_removed}."
        warn_msg = prefix + main_message + postfix
        print(warn_msg)
        return func(*args, **kwargs)

    return wrapper

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def sum(x, y):
    return x + y

@deprecated
def subst(x, y):
    return x - y

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def foo():
    print("Hello from foo")

@deprecated(since="of the Earth with dinosaurs")
def bar():
    print("Hello from bar")

@deprecated(will_be_removed="when pigs fly")
def baz():
    print("Hello from baz")

# Testing the functions
result = sum(4, 6)
print(result)

result = subst(7, 1)
print(result)

foo()
bar()
baz()
