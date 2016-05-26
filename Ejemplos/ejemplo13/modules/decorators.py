from functools import wraps


def int_transformer(func):
    """
    Decorator de funcion transforma un valor decimal a un entero
    :param func:
    :type func:
    :return:
    :rtype:
    """

    @wraps(func)
    def wrapper(arg):
        ret = func(arg)
        return int(ret)

    return wrapper
