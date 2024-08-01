def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs.get("magicnumber") == 7
