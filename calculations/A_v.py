import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def A_v(A_matrix: np.array, v_0: Callable, v_G: Callable, S0: np.array, T: float) -> np.array:
    """

    :param A_matrix: np.array with elements A11, A12, A21, A22
    :param v_0: function of two arguments x, t
    :param v_G: function of two arguments x, t
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space-time domain
    :param T: float greater that zero - Max time value
    :return: np.array matrix of floats with L0*R0 + LG*RG rows and 1 col
    """

    A = abs(S0[0][0]) - S0[0][0]
    B = abs(S0[-1][1]) + S0[-1][1]
    T_0 = -T

    A11, A12, A21, A22 = A_matrix[0], A_matrix[1], A_matrix[2], A_matrix[3]

    A_v0 = []
    A_vG = []

    for i in range(A11.size):
        def integrand1(x: float, t: float) -> float:
            return A11[i][0](x, t) * v_0(x, t)

        def integrand2(x: float, t: float) -> float:
            return A12[i][0](x, t) * v_G(x, t)

        integral = 0.0
        for ii in range(len(S0)):
            integral += dblquad(integrand1, T_0, 0, lambda t: S0[ii][0], lambda t: S0[ii][1])[
                0]  # Sec value is precision

        integral += dblquad(integrand2, 0, T, lambda t: A, lambda t: S0[0][0])[0]

        for iii in range(1, len(S0) - 1):
            integral += dblquad(integrand2, 0, T, lambda t: S0[iii][1], lambda t: S0[iii + 1][0])[
                0]  # Sec value is precision

        integral += dblquad(integrand2, 0, T, lambda t: S0[-1][1], lambda t: B)[0]

        A_v0.append(integral)

    for j in range(A21.size):
        def integrand1(x: float, t: float) -> float:
            return A21[j][0](x, t) * v_0(x, t)

        def integrand2(x: float, t: float) -> float:
            return A22[j][0](x, t) * v_G(x, t)

        integral = 0.0
        for jj in range(len(S0)):
            integral += dblquad(integrand1, T_0, 0, lambda t: S0[jj][0], lambda t: S0[jj][1])[
                0]  # Sec value is precision

        integral += dblquad(integrand2, 0, T, lambda t: A, lambda t: S0[0][0])[0]

        for jjj in range(1, len(S0) - 1):
            integral += dblquad(integrand2, 0, T, lambda t: S0[jjj][1], lambda t: S0[jjj + 1][0])[
                0]  # Sec value is precision

        integral += dblquad(integrand2, 0, T, lambda t: S0[-1][1], lambda t: B)[0]

        A_vG.append(integral)

    A_v = []
    for k in range(A11.size):
        A_v.append([A_v0[k]])
    for kk in range(A21.size):
        A_v.append([A_vG[kk]])

    return np.array(A_v)
