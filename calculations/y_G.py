import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def y_G(G: Callable, SG: np.array, T: float, u_G: Callable) -> Callable:
    """

    :param G: function of two variables x, t - Green's function
    :param SG: has next form: np.array([[c0, d0],...,[c_last, d_last]) - Boundary space domain
    :param T: float greater that zero - Max time value
    :param u_G: function of two variables x, t
    :return: function of two variables x, t
    """

    C = abs(SG[0][0]) - SG[0][0]
    D = abs(SG[-1][1]) + SG[-1][1]

    def res(x: float, t: float) -> float:
        def integrand(x_: float,
                      t_: float) -> float:  # For using in scipy.integrate.dblquad and in formula G(x-x', t-t')u(x',t')
            return G(x - x_, t - t_) * u_G(x_, t_)

        integral = 0.0
        integral += dblquad(integrand, T, 0, lambda t_: C,
                            lambda t_: SG[0][0])[0]

        for e in range(1, len(SG) - 1):
            integral += dblquad(integrand, T, 0, lambda t_: SG[e][1], lambda t_: SG[e + 1][0])[
                0]  # Sec value is precision

        integral += dblquad(integrand, T, 0,
                            lambda t_: SG[-1][1], lambda t_: D)[0]

        return integral

    return res
