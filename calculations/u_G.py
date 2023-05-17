from numpy import array, block
from numpy.linalg import pinv
from typing import Callable


def u_G(A_matrix: array, P: array, Y_slash: array, A_v: array, v_G: Callable) -> Callable:
    """

    :param A_matrix: np.array with elements A21, A22, A31, A32
    :param P: np.array square matrix of floats P with LG*RG + sum(Ji, i=1..I) dimension
    :param Y_slash: np.array matrix of floats with LG*RG + sum(Ji, i=1..I) rows and 1 col
    :param A_v: np.array matrix of floats with LG*RG + sum(Ji, i=1..I) rows and 1 col
    :param v_G: function of two variables x, t
    :return: u_G function of two variables x, t
    """

    def calculate_matrix(matrix: array, x: float, t: float) -> array:
        calculated = [[matrix[row_][col_](x, t) for col_ in range(len(matrix[row_]))]
                      for row_ in range(len(matrix))]
        return array(calculated)

    def A_2(x: float, t: float) -> array:
        A_2_matrix = block(
            [A_matrix[1].transpose(), A_matrix[3].transpose()])
        return calculate_matrix(A_2_matrix, x, t)

    P_inv = pinv(P)

    def res(x: float, t: float) -> float:
        matrix_part = A_2(x, t) @ P_inv @ (Y_slash - A_v)  # Matrix 1x1
        return matrix_part[0][0] + v_G(x, t)

    return res
