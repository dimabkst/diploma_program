import numpy as np
from typing import Callable


def Y_slash(y_infinity: Callable, LrG_list: np.array, slG_list: np.array, YrlG_list: np.array,
            Li_list: np.array, sij_list: np.array, Yij_list: np.array, ) -> np.array:
    """
    :param y_infinity: function of two variables x, t
    :param LrG_list: np.array of LrG differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param slG_list: np.array of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :param YrlG_list: np.array of np.arrays of YrlG that is float: [[Y11G, Y12G, ...], ...]
    :param Li_list: list of Li differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param sij_list: np.array of np.arrays of of sij that is np.array of two float values x and t: [[[x00, t00], [x01, t01], ...], ...]
    :param Yij_list: np.array of np.arrays of Yij that is float: [[Y11, Y12, ...], ...]
    :return: np.array matrix of floats with LG*RG + (sum(Ji, i=1..I)) * I rows and 1 col
    """
    I = len(Li_list)
    Ji = [len(sij_list[i]) for i in range(I)]

    L_G = len(slG_list)
    R_G = len(LrG_list)

    Ypl = []
    for ro in range(R_G):
        LrG_y_inf = LrG_list[ro](y_infinity)
        for l in range(L_G):
            Ypl.append(YrlG_list[ro][l] -
                       LrG_y_inf(slG_list[l][0], slG_list[l][1]))

    Ystar = []
    for i in range(I):
        Li_y_inf = Li_list[i](y_infinity)
        for j in range(Ji[i]):
            Ystar.append(Yij_list[i][j] -
                         Li_y_inf(sij_list[i][j][0], sij_list[i][j][1]))

    result = []
    for pl in range(R_G * L_G):
        result.append([Ypl[pl]])
    for ij in range(I * sum(Ji)):
        result.append([Ystar[ij]])

    return np.array(result)
