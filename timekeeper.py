from collections import defaultdict
import time


class TimeKeeper(object):
    def __init__(self):
        self.reset()

    def time(self, name):
        def decorator(fn):
            def inner(*args, **kwargs):
                start = time.time()
                ret = fn(*args, **kwargs)
                end = time.time()
                self._profile[name] += (end-start)
            return inner
        return decorator

    def profile(self):
        return self._profile

    def reset(self):
        self._profile = defaultdict(float)
