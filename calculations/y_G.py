import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def y_G(G: Callable, S0: np.array, T: float, u_G: Callable) -> Callable:
    """

    :param G: function of two variables x, t - Green's function
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space-time domain
    :param T: float greater that zero - Max time value
    :param u_G: function of two variables x, t
    :return: function of two variables x, t
    """

    A = abs(S0[0][0]) - S0[0][0]
    B = abs(S0[-1][1]) + S0[-1][1]

    def res(x: float, t: float) -> float:
        def integrand(x_: float,
                      t_: float) -> float:  # For using in scipy.integrate.dblquad and in formula G(x-x', t-t')u(x',t')
            return G(x - x_, t - t_) * u_G(x_, t_)

        integral = 0.0
        integral += dblquad(integrand, T, 0, lambda t_: A, lambda t_: S0[0][0])[0]

        for i in range(1, len(S0) - 1):
            integral += dblquad(integrand, T, 0, lambda t_: S0[i][1], lambda t_: S0[i + 1][0])[
                0]  # Sec value is precision

        integral += dblquad(integrand, T, 0, lambda t_: S0[-1][1], lambda t_: B)[0]

        return integral

    return res
