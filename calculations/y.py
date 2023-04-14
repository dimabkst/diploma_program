from typing import Callable


def y(y_infinity: Callable, y_0: Callable, y_G: Callable) -> Callable:
    """

    :param y_infinity: function of two variables
    :param y_0: function of two variables
    :param y_G: function of two variables
    :return: function of two variables
    """

    def res(x: float, t: float) -> float:
        return y_infinity(x, t) + y_0(x, t) + y_G(x, t)

    return res
