import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def y_0(G: Callable, S0: np.array, T: float, u_0: Callable) -> Callable:
    """

    :param G: function of two variables x, t - Green's function
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space domain
    :param T: float greater that zero - Max time value
    :param u_0: function of two variables x, t
    :return: function of two variables x, t
    """

    T_0 = -T

    def res(x: float, t: float) -> float:
        def integrand(x_: float,
                      t_: float) -> float:  # For using in scipy.integrate.dblquad and in formula G(x-x', t-t')u(x',t')
            return G(x - x_, t - t_) * u_0(x_, t_)

        integral = 0.0
        for k in range(len(S0)):
            integral += dblquad(integrand, T_0, 0, lambda t_: S0[k][0], lambda t_: S0[k][1])[
                0]  # Sec value is precision

        return integral

    return res
