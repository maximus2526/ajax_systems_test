# 1:
# Написать функцию, которая конвертирует Decimal Degrees (DD) формат координат
# в Degrees Decimal Minutes (DDM) формат координат

# 2:
# С помощью pytest написать параметризированный тест, который принимает на
# вход значение в DD формате и ожидаемое значение
# в DDM формате

from math import floor, trunc  # Округление чисел в меньшую сторону
import pytest


def convert_DD_to_DDM(DD: float):
    """
    a°b'c" = (a + b/60 + c/3600)°
    :param DD - Decimal Degrees:
    :return DDM str:
    """
    degrees = trunc(DD)
    minutes = round((DD - degrees) * 60, 3)
    seconds = round((DD - degrees - minutes / 60) * 3600)
    return abs(degrees), abs(minutes), abs(seconds)


if __name__ == "__main__":
    print(convert_DD_to_DDM(0.4))
