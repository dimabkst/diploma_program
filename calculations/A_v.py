import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def A_v(A_matrix: np.array, v_0: Callable, v_G: Callable, S0: np.array, SG: np.array, T: float, integrals_precision: float) -> np.array:
    """

    :param A_matrix: np.array with elements A21, A22, A31, A32
    :param v_0: function of two arguments x, t
    :param v_G: function of two arguments x, t
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]]) - Initial space domain
    :param SG: has next form: np.array([[c0, d0],...,[c_last, d_last]]) - Boundary space domain
    :param T: float greater that zero - Max time value
    :param integrals_precision: dblquad integrals precision
    :return: np.array matrix of floats with LG*RG + (sum(Ji, i=1..I)) * I rows and 1 col
    """

    C = SG[0][0] - abs(SG[0][0])
    D = SG[-1][1] + abs(SG[-1][1])
    T_0 = -T

    A21, A22, A31, A32 = A_matrix[0], A_matrix[1], A_matrix[2], A_matrix[3]

    A_v0 = []
    A_vG = []

    for rowNum in range(A21.size):
        def integrand1(x: float, t: float) -> float:
            return A21[rowNum][0](x, t) * v_0(x, t)

        def integrand2(x: float, t: float) -> float:
            return A22[rowNum][0](x, t) * v_G(x, t)

        integral = 0.0
        for k in range(len(S0)):
            integral += dblquad(integrand1, T_0, 0, lambda t: S0[k][0], lambda t: S0[k][1], epsabs=integrals_precision, epsrel=integrals_precision)[
                0]  # Sec value is precision

        integral += dblquad(integrand2, 0, T, lambda t: C,
                            lambda t: SG[0][0], epsabs=integrals_precision, epsrel=integrals_precision)[0]

        for e in range(1, len(SG) - 1):
            integral += dblquad(integrand2, 0, T, lambda t: SG[e][1], lambda t: S0[e + 1][0], epsabs=integrals_precision, epsrel=integrals_precision)[
                0]  # Sec value is precision

        integral += dblquad(integrand2, 0, T,
                            lambda t: SG[-1][1], lambda t: D, epsabs=integrals_precision, epsrel=integrals_precision)[0]

        A_v0.append(integral)

    for rowNum in range(A31.size):
        def integrand1(x: float, t: float) -> float:
            return A31[rowNum][0](x, t) * v_0(x, t)

        def integrand2(x: float, t: float) -> float:
            return A32[rowNum][0](x, t) * v_G(x, t)

        integral = 0.0
        for k in range(len(S0)):
            integral += dblquad(integrand1, T_0, 0, lambda t: S0[k][0], lambda t: S0[k][1], epsabs=integrals_precision, epsrel=integrals_precision)[
                0]  # Sec value is precision

        integral += dblquad(integrand2, 0, T, lambda t: C,
                            lambda t: SG[0][0], epsabs=integrals_precision, epsrel=integrals_precision)[0]

        for e in range(1, len(SG) - 1):
            integral += dblquad(integrand2, 0, T, lambda t: SG[e][1], lambda t: SG[e + 1][0], epsabs=integrals_precision, epsrel=integrals_precision)[
                0]  # Sec value is precision

        integral += dblquad(integrand2, 0, T,
                            lambda t: SG[-1][1], lambda t: D, epsabs=integrals_precision, epsrel=integrals_precision)[0]

        A_vG.append(integral)

    A_v = []
    for pl in range(A21.size):
        A_v.append([A_v0[pl]])
    for ij in range(A31.size):
        A_v.append([A_vG[ij]])

    return np.array(A_v)
