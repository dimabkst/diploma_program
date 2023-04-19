import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def P(A_matrix: np.array, S0: np.array, SG: np.array, T: float) -> np.array:
    """

    :param A_matrix: np.array with elements A21, A22, A31, A32
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space-time domain
    :param SG: has next form: np.array([[c0, d0],...,[c_last, d_last]]) - Boundary space domain
    :param T: float greater that zero - Max time value
    :return: np.array square matrix of P21, P22, P31, P32 matrices
    """

    C = abs(SG[0][0]) - SG[0][0]
    D = abs(SG[-1][1]) + SG[-1][1]
    T_0 = -T

    P_parts = []

    def calculate_matrix(matrix: np.array, x: float, t: float) -> np.array:
        res = [[matrix[row_][col_](x, t) for col_ in range(
            len(matrix[row_]))] for row_ in range(len(matrix))]
        return np.array(res)

    for n in range(2):  # n is n-2 in file due to original n be from 2 to 3
        for m in range(2):  # m is m-1 in file
            # These are matrix An1, Am1 from pdf file with math
            P_nm_dim = [len(A_matrix[2 * n]), len(A_matrix[2 * m])]
            P_parts.append([[[] for __ in range(P_nm_dim[1])]
                           for _ in range(P_nm_dim[0])])

            def integrand1(row_: int, col_: int) -> Callable:
                def temp(x: float, t: float) -> float:
                    An1 = calculate_matrix(A_matrix[2 * n], x, t)
                    Am1T = calculate_matrix(A_matrix[2 * m], x, t).transpose()
                    return (An1 @ Am1T)[row_][col_]

                return temp

            def integrand2(row_: int, col_: int) -> Callable:
                def temp(x: float, t: float) -> float:
                    An2 = calculate_matrix(A_matrix[2 * n + 1], x, t)
                    Am2T = calculate_matrix(
                        A_matrix[2 * m + 1], x, t).transpose()
                    return (An2 @ Am2T)[row_][col_]

                return temp

            for row in range(P_nm_dim[0]):
                for col in range(P_nm_dim[1]):
                    integral = 0.0

                    for k in range(len(S0)):
                        # Sec value is precision
                        integral += dblquad(integrand1(row, col), T_0,
                                            0, lambda t: S0[k][0], lambda t: S0[k][1])[0]

                    integral += dblquad(integrand2(row, col),
                                        0, T, lambda t: C, lambda t: SG[0][0])[0]

                    for e in range(1, len(SG) - 1):
                        # Sec value is precision
                        integral += dblquad(integrand2(row, col), 0, T,
                                            lambda t: SG[e][1], lambda t: SG[e + 1][0])[0]

                    integral += dblquad(integrand2(row, col),
                                        0, T, lambda t: SG[-1][1], lambda t: D)[0]

                    P_parts[-1][row][col] = integral

    for i in range(len(P_parts)):
        P_parts[i] = np.array(P_parts[i])

    return np.block([
        [P_parts[0], P_parts[1]],
        [P_parts[2], P_parts[3]]
    ])
