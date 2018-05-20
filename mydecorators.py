import collections
import functools
import time
import types
import signal

def trace(func):
    """
    print common debug points
        : arguments taken
        : result of return
    """
    @functools.wraps(func) # access to func.__name__ , __doc__
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() 'f'returned {original_result!r}')
        return original_result
    return wrapper

def timer(func):
    """
    : time function execution
    """
    def wrapper(*arg):
        t = time.clock()
        res = func(*arg)
        print(func.func_name, time.clock()-t)
        return res
    return wrapper

class Timeout(Exception): pass
def timeout(seconds, error_message='Function call timed out'):
    """
    :param seconds: how long until triggering timeout
    :param error_message: change error message
    :return: function stoppage
    Usage:
        import time
        @timeout(1, 'too fin slow')
        def slow_function():
            time.sleep(5)
    """
    def decorate(func):
        def _handle_timeout(signal, frame):
            raise TimeoutError(error_message)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return functools.wraps(func)(wrapper)
    return decorate

class memoized(object):
    """
    Memoize function
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

def addto(className):
    """
    :param className: name of class
    :return: adds method to class instance

    Usage:
        class Foo:
            def __init__(self):
                self.x = 69

        foo = Foo()

        @addto(foo)
        def print_x(self):
            print self.x
        # foo.print_x() now prints 69
    """
    def wrapper(func):
        func = types.MethodType(func, className, className.__class__)
        setattr( className, func.func_name, func )
        return func
    return wrapper

def synch(lock):
    """
    :param lock: lock instance
    :return: synchronize 2+ functions on a lock
    Usage:
        from threading import Lock
        my_lock = Lock()
        @synch(my_lock)
        def func_one():
            pass
        #synch(my_lock)
        def func_two():
            pass
    """
    def wrap(f):
        def hold(*args, **kwargs):
            lock.acquire()
            try:
                return f(*args, **kwargs)
            finally:
                lock.release()
        return hold
    return wrap
