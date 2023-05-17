from numpy import array
from typing import Callable


def Yij(y: Callable, Li_list: array, sij_list: array) -> array:
    """

    :param y: function of two variables x, t
    :param Li_list: list of Li differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param sij_list: np.array of np.arrays of of sij that is np.array of two float values x and t: [[[x00, t00], [x01, t01], ...], ...]
    :return: np.array of np.arrays of Yij that is float: [[Y11, Y12, ...], ...]
    """

    try:
        I = len(Li_list)

        res = []
        for i in range(I):
            res.append([])
            for sij in sij_list[i]:
                res[-1].append(Li_list[i](y)(sij[0], sij[1]))

        res = array(res, dtype=object)

        return res
    except Exception as e:
        raise e
