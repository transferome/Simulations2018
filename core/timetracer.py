"""Time Decorator which Traces The Input Function With A Label Provided By the Caller"""
import time


def timer(label='generic_func', trace=True):
    """Function acts as wrapper to decorate the timer class object"""
    class Timer:

        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format_time = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format_time % values)
            return result
    return Timer


if __name__ == '__main__':
    pass
