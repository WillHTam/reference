import argument_decorator

@argument_decorator.trace
def addition(x, y):
    return x + y


print( addition(1,2) )