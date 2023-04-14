import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def y_infinity(G: Callable, u: Callable, S0: np.array, T: float) -> Callable:
    """

    :param G: function of two variables x, t - Green's function
    :param u: function of two variables x, t - Disturbance
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space-time domain
    :param T: float greater that zero - Max time value
    :return: function of two variables x, t
    """

    def res(x: float, t: float) -> float:
        def integrand(x_: float,
                      t_: float) -> float:  # For using in scipy.integrate.dblquad and in formula G(x-x', t-t')u(x',t')
            return G(x - x_, t - t_) * u(x_, t_)

        integral = 0.0
        for i in range(len(S0)):
            integral += dblquad(integrand, 0, T, lambda t_: S0[i][0], lambda t_: S0[i][1])[0]  # Sec value is precision

        return integral

    return res
