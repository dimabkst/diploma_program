import numpy as np
from typing import Callable


def u_G(A_matrix: np.array, P: np.array, Y_slash: np.array, A_v: np.array, v_G: Callable) -> Callable:
    """

    :param A_matrix: np.array with elements A11, A12, A21, A22
    :param P: np.array square matrix of floats P with L0*RO + LG*RG dimension
    :param Y_slash: np.array matrix of floats with L0*R0 + LG*RG rows and 1 col
    :param A_v: np.array with L0*R0 + LG*RG rows and 1 col
    :param v_G: function of two variables x, t
    :return: u_G function of two variables x, t
    """

    def calculate_matrix(matrix: np.array, x: float, t: float) -> np.array:
        calculated = [[matrix[row_][col_](x, t) for col_ in range(len(matrix[row_]))] for row_ in range(len(matrix))]
        return np.array(calculated)

    def A_G(x: float, t: float) -> np.array:
        A_G_matrix = np.block([A_matrix[1].transpose(), A_matrix[3].transpose()])
        return calculate_matrix(A_G_matrix, x, t)

    P_inv = np.linalg.pinv(P)

    def res(x: float, t: float) -> float:
        matrix_part = A_G(x, t) @ P_inv @ (Y_slash - A_v)  # Matrix 1x1
        return matrix_part[0][0] + v_G(x, t)

    return res
