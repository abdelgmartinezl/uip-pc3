import math as mah
from decorators import int_transformer


@int_transformer
def seconds(ms):
    """
    Calcula milisegundo(s) a segundo(s)
    :param ms:
    :type ms:
    :return: Segundo(s)
    :rtype: int
    """
    return ms / 1000

@int_transformer
def minutes(s):
    """
    Calcula segundo(s) a minutos(s)
    :param s:
    :type s:
    :return:
    :rtype:
    """
    return s / 60

def hours(m):
    """
    Calcula minuto(s) a hora(s)
    :param m:
    :type m:
    :return:
    :rtype:
    """
    return mah.floor(m / 60)


def days(hr):
    """
    Calcula hora(s) a dia(s)
    :param hr: Hora(s)
    :type hr: int
    :return: Dia(s) es un entero mas grande pero menor o igual `hr`
    :rtype: int
    """
    return mah.floor(hr / 24)
