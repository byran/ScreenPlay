import functools
import time


def retry_until(expected: any, time_out_secs: float = 5, interval_secs: float = 0.5):
    def decorator_retry_until(func):
        @functools.wraps(func)
        def wrapper_retry_until(*args, **kwargs):
            start_time = time.time()
            value = func(*args, **kwargs)

            while value != expected and ((time.time() - start_time) <= time_out_secs):
                time.sleep(interval_secs)
                value = func(*args, **kwargs)

            return value
        return wrapper_retry_until
    return decorator_retry_until
