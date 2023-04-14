import numpy as np
from typing import Callable
from scipy.integrate import dblquad


def P(A_matrix: np.array, S0: np.array, T: float) -> np.array:
    """

    :param A_matrix: np.array with elements A11, A12, A21, A22
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space-time domain
    :param T: float greater that zero - Max time value
    :return: np.array square matrix of P11, P12, P21, P22 matrices
    """

    A = abs(S0[0][0]) - S0[0][0]
    B = abs(S0[-1][1]) + S0[-1][1]
    T_0 = -T

    P_parts = []

    def calculate_matrix(matrix: np.array, x: float, t: float) -> np.array:
        res = [[matrix[row_][col_](x, t) for col_ in range(len(matrix[row_]))] for row_ in range(len(matrix))]
        return np.array(res)

    for i in range(2):
        for j in range(2):
            P_ij_dim = [len(A_matrix[2 * i]), len(A_matrix[2 * j])]  # It's matrix Ai1 from pdf file with math
            P_parts.append([[[] for __ in range(P_ij_dim[1])] for _ in range(P_ij_dim[0])])

            def integrand1(row_: int, col_: int) -> Callable:
                def temp(x: float, t: float) -> float:
                    Ai1 = calculate_matrix(A_matrix[2 * i], x, t)
                    Aj1T = calculate_matrix(A_matrix[2 * j], x, t).transpose()
                    return (Ai1 @ Aj1T)[row_][col_]

                return temp

            def integrand2(row_: int, col_: int) -> Callable:
                def temp(x: float, t: float) -> float:
                    Ai2 = calculate_matrix(A_matrix[2 * i + 1], x, t)
                    Aj2T = calculate_matrix(A_matrix[2 * j + 1], x, t).transpose()
                    return (Ai2 @ Aj2T)[row_][col_]

                return temp

            for row in range(P_ij_dim[0]):
                for col in range(P_ij_dim[1]):
                    integral = 0.0

                    for ii in range(len(S0)):
                        integral += dblquad(integrand1(row, col), T_0, 0, lambda t: S0[ii][0], lambda t: S0[ii][1])[
                            0]  # Sec value is precision

                    integral += dblquad(integrand2(row, col), 0, T, lambda t: A, lambda t: S0[0][0])[0]

                    for iii in range(1, len(S0) - 1):
                        integral += dblquad(integrand2(row, col), 0, T, lambda t: S0[iii][1], lambda t: S0[iii + 1][0])[
                            0]  # Sec value is precision

                    integral += dblquad(integrand2(row, col), 0, T, lambda t: S0[-1][1], lambda t: B)[0]

                    P_parts[-1][row][col] = integral

    for i in range(len(P_parts)):
        P_parts[i] = np.array(P_parts[i])

    return np.block([
        [P_parts[0], P_parts[1]],
        [P_parts[2], P_parts[3]]
    ])
