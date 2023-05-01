from typing import Callable
import numpy as np


def Yrl0(y: Callable, Lr0_list: np.array, xl0_list: np.array) -> np.array:
    """

    :param y: function of two variables x, t
    :param Lr0_list: list of Lr0 differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param xl0_list: list of float xl0: [x0, x1, x2, ...]
    :return: np.array of np.arrays of Yrl0 that is float: [[Y110, Y120, ...], ...]
    """

    try:
        R0 = len(Lr0_list)
        L0 = len(xl0_list)

        res = []
        for r in range(R0):
            res.append([])
            for l in range(L0):
                res[-1].append(Lr0_list[r](y)(xl0_list[l], 0))

        res = np.array(res)

        return res
    except Exception as e:
        raise e
