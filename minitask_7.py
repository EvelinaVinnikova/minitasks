import functools

def deprecated(since = None, will_be_removed = None):
    if callable(since):
        func = since

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warn_mssg = f"Warning: function {func.__name__} is deprecated. It will be removed in future versions."
            print(warn_mssg)
            return func(*args, **kwargs), warn_mssg

        return wrapper

    def inner(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            prefix = f"Warning: function {f.__name__} is deprecated"
            main_message = f"."
            postfix = f" It will be removed in future versions."
            if since:
                main_message = f" since version {since}."
            if will_be_removed:
                postfix = f" It will be removed in version {will_be_removed}."
            warn_mssg = prefix + main_message + postfix
            print(warn_mssg)
            return f(*args, **kwargs), warn_mssg
        return wrapper
    return inner

@deprecated(since= "4.2.0", will_be_removed= "5.0.1")
def sum(x, y):
    return x+y

@deprecated
def subst(x, y):
    return x-y
print(subst(7,1))
@deprecated(since= "4.2.0", will_be_removed= "5.0.1")
def foo():
    print("Hello from foo")

@deprecated(since= "of the Earth with dinosaurs")
def bar():
    print("Hello from bar")

@deprecated(will_be_removed= "when pig fly")
def baz():
    print("Hello from baz")

result, warning = sum(4, 6)
assert warning == "Warning: function sum is deprecated since version 4.2.0. It will be removed in version 5.0.1."
print(result)
result, warning = subst(7, 1)
assert warning == "Warning: function subst is deprecated. It will be removed in future versions."
print(result)
result, warning = foo()
assert warning == "Warning: function foo is deprecated since version 4.2.0. It will be removed in version 5.0.1."
result, warning = bar()
assert warning == "Warning: function bar is deprecated since version of the Earth with dinosaurs. It will be removed in future versions."
result, warning = baz()
assert warning == "Warning: function baz is deprecated. It will be removed in version when pig fly."
