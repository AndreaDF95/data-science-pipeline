import time
from functools import wraps


def retry(max_attempts=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[Retry] Attempt {attempt} failed: {e}")

                    if attempt == max_attempts:
                        raise

                    time.sleep(delay)

        return wrapper

    return decorator
