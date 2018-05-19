# decorators from simple_ and multiple_ will not not work on a function 
# that takes arguments

# use *args and **kwargs 
# will use * and ** to collect all positional and keyword arguments to store in variables
# decorator then forwards the collected arguments to the original input argument

def trace(func):
    @functools.wraps(func)
    # since the function called with a decorator is a new function
    # without @functools.wraps, using say.__name__ or say.__doc__
    # to see the doctstring would not work
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
            f'with {args}, {kwargs}')
        
        original_result = func(*args, **kwargs) 
        
        print(f'TRACE: {func.__name__}() 'f'returned {original_result!r}')
        
        return original_result 

    return wrapper

@trace
def say(name, line):
    """ name says line """
    return f'{name}: {line}'

if __name__ == '__main__':
    print( say('Wombat', 'Hellou') )
