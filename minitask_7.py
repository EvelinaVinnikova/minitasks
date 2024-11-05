def deprecated(since = None, will_be_removed = None):
    def inner(f):
        def wrapper(*args, **kwargs):
            if since and will_be_removed:
                warn_mssg = f"Warning: function {f.__name__} is deprecated since version {since}. It will be removed in version {will_be_removed}."
            elif will_be_removed:
                warn_mssg = f"Warning: function {f.__name__} is deprecated. It will be removed in version {will_be_removed}."
            elif since:
                warn_mssg = f"Warning: function {f.__name__} is deprecated since version {since}. It will be removed in future versions."
            else:
                warn_mssg = f"Warning: function {f.__name__} is deprecated. It will be removed in future versions."
            print(warn_mssg)
            return f(*args, **kwargs), warn_mssg
        return wrapper
    return inner

@deprecated(since= "4.2.0", will_be_removed= "5.0.1")
def foo():
    print("Hello from foo")

@deprecated(since= "of the Earth with dinosaurs")
def bar():
    print("Hello from bar")

@deprecated(will_be_removed= "when pig fly")
def baz():
    print("Hello from baz")


result, warning = foo()
assert warning == "Warning: function foo is deprecated since version 4.2.0. It will be removed in version 5.0.1."
result, warning = bar()
assert warning == "Warning: function bar is deprecated since version of the Earth with dinosaurs. It will be removed in future versions."
result, warning = baz()
assert warning == "Warning: function baz is deprecated. It will be removed in version when pig fly."
