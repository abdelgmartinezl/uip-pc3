import math as mah
from decorators import dtype_int


@dtype_int
def seconds(ms):
    """
    Calcula milisegundo(s) a segundo(s)
    :param ms:
    :type ms:
    :return: Segundo(s)
    :rtype: int
    """
    return ms / 1000


@dtype_int
def minutes(s):
    """
    Calcula segundo(s) a minutos(s)
    :param s:
    :type s:
    :return:
    :rtype:
    """
    return s / 60


@dtype_int
def hours(m):
    """
    Calcula minuto(s) a hora(s)
    :param m:
    :type m:
    :return:
    :rtype:
    """
    return mah.floor(m / 60)


@dtype_int
def days(hr):
    """
    Calcula hora(s) a dia(s)
    :param hr: Hora(s)
    :type hr: int
    :return: Dia(s) es un entero mas grande pero menor o igual `hr`
    :rtype: int
    """
    return mah.floor(hr / 24)
