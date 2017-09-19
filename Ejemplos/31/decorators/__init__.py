def dtype_int(func):
    """
    Factory decorator toma una función casting a tipo entero
    :param func: 
    :return: 
    """
    from functools import wraps

    @wraps(func)
    def wrapper(arg):
        ret = func(arg)
        return int(ret)

    return wrapper
