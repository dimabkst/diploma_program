from numpy import array
from numpy.linalg import pinv


def precision(Y_slash: array, P: array) -> float:
    """

    :param Y_slash: np.array of A21, A22, A31, A32 that are np.arrays matrix of two variables functions
    :param P: np.array square matrix of P21, P22, P31, P32 matrices
    :return: float number that is epsilon square
    """

    P_inv = pinv(P)
    Y_slash_transpose = Y_slash.transpose()

    matrix_part = Y_slash_transpose @ Y_slash - \
        Y_slash_transpose @ P @ P_inv @ Y_slash

    result = matrix_part[0][0]

    return result
