from functools import wraps
NULL_VAL = 0


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(arg <= NULL_VAL for arg in args):
            raise ValueError("Все аргументы должны быть положительными.")
        if any(value <= NULL_VAL for value in kwargs.values()):
            raise ValueError("Все аргументы должны быть положительными.")
        return func(*args, **kwargs)
    return wrapper
