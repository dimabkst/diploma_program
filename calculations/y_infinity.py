import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def y_infinity(G: Callable, u: Callable, S0: np.array, T: float) -> Callable:
    """

    :param G: function of two variables x, t - Green's function
    :param u: function of two variables x, t - Disturbance
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space domain
    :param T: float greater that zero - Max time value
    :return: function of two variables x, t
    """

    def res(x: float, t: float) -> float:
        def integrand(x_: float,
                      t_: float) -> float:  # For using in scipy.integrate.dblquad and in formula G(x-x', t-t')u(x',t')
            return G(x - x_, t - t_) * u(x_, t_)

        integral = 0.0
        for k in range(len(S0)):
            # Sec value is precision
            integral += dblquad(integrand, 0, T,
                                lambda t_: S0[k][0], lambda t_: S0[k][1], epsabs=1.5e-1, epsrel=1.5e-1)[0]

        return integral

    return res
