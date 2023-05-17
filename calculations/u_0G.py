from numpy import array, block
from numpy.linalg import pinv
from typing import Callable, Tuple


def u_0G(A_matrix: array, P: array, Y_slash: array, A_v: array, v_0: Callable, v_G: Callable) -> Tuple[Callable, Callable]:
    """

    :param A_matrix: np.array with elements A21, A22, A31, A32
    :param P: np.array square matrix of floats P with LG*RG + sum(Ji, i=1..I) dimension
    :param Y_slash: np.array matrix of floats with LG*RG + sum(Ji, i=1..I) rows and 1 col
    :param A_v: np.array matrix of floats with LG*RG + sum(Ji, i=1..I) rows and 1 col
    :param v_0: function of two variables x, t
    :param v_G: function of two variables x, t
    :return: u_0, u_G function of two variables x, t
    """

    def calculate_matrix(matrix: array, x: float, t: float) -> array:
        calculated = [[matrix[row_][col_](x, t) for col_ in range(len(matrix[row_]))]
                      for row_ in range(len(matrix))]
        return array(calculated)

    def A_1(x: float, t: float) -> array:
        A_1_matrix = block(
            [A_matrix[0].transpose(), A_matrix[2].transpose()])
        return calculate_matrix(A_1_matrix, x, t)

    def A_2(x: float, t: float) -> array:
        A_2_matrix = block(
            [A_matrix[1].transpose(), A_matrix[3].transpose()])
        return calculate_matrix(A_2_matrix, x, t)

    P_inv = pinv(P)

    def u0_res(x: float, t: float) -> float:
        matrix_part = A_1(x, t) @ P_inv @ (Y_slash - A_v)  # Matrix 1x1
        return matrix_part[0][0] + v_0(x, t)

    def uG_res(x: float, t: float) -> float:
        matrix_part = A_2(x, t) @ P_inv @ (Y_slash - A_v)  # Matrix 1x1
        return matrix_part[0][0] + v_G(x, t)

    return u0_res, uG_res
