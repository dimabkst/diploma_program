import numpy as np
from typing import Callable


def A(G: Callable, LrG_list: np.array, slG_list: np.array, Li_list: np.array, sij_list: np.array) -> list:
    """

    :param G: function of two variables x, t - Green's function
    :param LrG_list: np.array of LrG differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param slG_list: np.array of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :param Li_list: list of Li differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param sij_list: np.array of np.arrays of of sij that is np.array of two float values x and t: [[[x00, t00], [x01, t01], ...], ...]
    :return: np.array of A21, A22, A31, A32 that are np.arrays matrix of two variables functions
    """

    L_G = len(slG_list)
    R_G = len(LrG_list)

    I = len(Li_list)
    Ji = [len(sij_list[i]) for i in range(I)]

    def func_wrapped_for_A(func: Callable, x: float, t: float) -> Callable:
        def shifted_func(x_, t_):
            return func(x - x_, t - t_)

        return shifted_func

    A21 = []
    for ro in range(R_G):
        for l in range(L_G):
            A21.append(
                [LrG_list[ro](func_wrapped_for_A(G, slG_list[l][0], slG_list[l][1]))])
    A21 = np.array(A21)
    A22 = np.copy(A21)

    A31 = []
    for i in range(I):
        for j in range(Ji[i]):
            A31.append([Li_list[i](func_wrapped_for_A(
                G, sij_list[i][j][0], sij_list[i][j][1]))])
    A31 = np.array(A31)
    A32 = np.copy(A31)

    return [A21, A22, A31, A32]
