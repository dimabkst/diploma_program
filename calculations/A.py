import numpy as np
from typing import Callable


def A(G: Callable, Lr0_list: np.array, xl0_list: np.array, LrG_list: np.array, slG_list: np.array) -> list:
    """

    :param G: function of two variables x, t - Green's function
    :param Lr0_list: np.array of Lr0 differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param xl0_list: np.array of float xl0: [x0, x1, x2, ...]
    :param LrG_list: np.array of LrG differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param slG_list: np.array of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :return: np.array of A11, A12, A21, A22 that are np.arrays matrix of two variables functions
    """

    L_0 = len(xl0_list)
    R_0 = len(Lr0_list)

    L_G = len(slG_list)
    R_G = len(LrG_list)

    def func_wrapped_for_A(func: Callable, x: float, t: float) -> Callable:
        def shifted_func(x_, t_):
            return func(x - x_, t - t_)

        return shifted_func

    A11 = []
    for i in range(R_0):
        for j in range(L_0):
            A11.append([Lr0_list[i](func_wrapped_for_A(G, xl0_list[j], 0))])
    A11 = np.array(A11)
    A12 = A11

    A21 = []
    for i in range(R_G):
        for j in range(L_G):
            A21.append([LrG_list[i](func_wrapped_for_A(G, slG_list[j][0], slG_list[j][1]))])
    A21 = np.array(A21)
    A22 = A21

    return [A11, A12, A21, A22]
