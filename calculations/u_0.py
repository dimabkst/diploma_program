from numpy import array, block
from numpy.linalg import pinv
from typing import Callable


def u_0(A_matrix: array, P: array, Y_slash: array, A_v: array, v_0: Callable) -> Callable:
    """

    :param A_matrix: np.array with elements A21, A22, A31, A32
    :param P: np.array square matrix of floats P with LG*RG + sum(Ji, i=1..I) dimension
    :param Y_slash: np.array matrix of floats with LG*RG + sum(Ji, i=1..I) rows and 1 col
    :param A_v: np.array matrix of floats with LG*RG + sum(Ji, i=1..I) rows and 1 col
    :param v_0: function of two variables x, t
    :return: u_0 function of two variables x, t
    """

    def calculate_matrix(matrix: array, x: float, t: float) -> array:
        calculated = [[matrix[row_][col_](x, t) for col_ in range(len(matrix[row_]))]
                      for row_ in range(len(matrix))]
        return array(calculated)

    def A_1(x: float, t: float) -> array:
        A_1_matrix = block(
            [A_matrix[0].transpose(), A_matrix[2].transpose()])
        return calculate_matrix(A_1_matrix, x, t)

    P_inv = pinv(P)

    def res(x: float, t: float) -> float:
        matrix_part = A_1(x, t) @ P_inv @ (Y_slash - A_v)  # Matrix 1x1
        return matrix_part[0][0] + v_0(x, t)

    return res
