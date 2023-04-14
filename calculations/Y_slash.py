import numpy as np
from typing import Callable


def Y_slash(y_infinity: Callable, Lr0_list: np.array, xl0_list: np.array, Yrl0_list: np.array,
            LrG_list: np.array, slG_list: np.array, YrlG_list: np.array, ) -> np.array:
    """
    :param y_infinity: function of two variables x, t
    :param Lr0_list: np.array of Lr0 differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param xl0_list: np.array of float xl0: [x0, x1, x2, ...]
    :param Yrl0_list: np.array of np.arrays of Yrl0 that is float: [[Y110, Y120, ...], ...]
    :param LrG_list: np.array of LrG differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param slG_list: np.array of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :param YrlG_list: np.array of np.arrays of YrlG that is float: [[Y11G, Y12G, ...], ...]
    :return: np.array matrix of floats with L0*R0 + LG*RG rows and 1 col
    """
    L_0 = len(xl0_list)
    R_0 = len(Lr0_list)

    L_G = len(slG_list)
    R_G = len(LrG_list)

    Yrl = []
    for i in range(R_0):
        for j in range(L_0):
            Yrl.append(Yrl0_list[i][j] - Lr0_list[i](y_infinity)(xl0_list[j], 0))

    Ypl = []
    for i in range(R_G):
        for j in range(L_G):
            Ypl.append(YrlG_list[i][j] - LrG_list[i](y_infinity)(slG_list[j][0], slG_list[j][1]))

    result = []
    for ii in range(R_0 * L_0):
        result.append([Yrl[ii]])
    for jj in range(R_G * L_G):
        result.append([Ypl[jj]])

    return np.array(result)
