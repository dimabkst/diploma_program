from numpy import array
from typing import Callable
from scipy.integrate import dblquad


def y_infinity(G: Callable, u: Callable, S: array, T: float, integrals_precision: float) -> Callable:
    """

    :param G: function of two variables x, t - Green's function
    :param u: function of two variables x, t - Disturbance
    :param S: has next form: np.array([[f0, g0],...,[f_last, g_last]]) - Space domain
    :param T: float greater that zero - Max time value
    :param integrals_precision: dblquad integrals precision
    :return: function of two variables x, t
    """

    def res(x: float, t: float) -> float:
        def integrand(x_: float,
                      t_: float) -> float:  # For using in scipy.integrate.dblquad and in formula G(x-x', t-t')u(x',t')
            return G(x - x_, t - t_) * u(x_, t_)

        integral = 0.0
        for h in range(len(S)):
            # Sec value is precision
            integral += dblquad(integrand, 0, T,
                                lambda t_: S[h][0], lambda t_: S[h][1], epsabs=integrals_precision, epsrel=integrals_precision)[0]

        return integral

    return res
