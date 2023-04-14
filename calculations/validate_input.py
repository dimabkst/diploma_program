from typing import Callable
import numpy as np


# Do not let segments intersect even in in boundaries,
# because do not know if integrals would be calculated correctly
def segments_intersect(segment1: np.array, segment2: np.array) -> bool:
    a1, b1 = segment1[0], segment1[1]
    a2, b2 = segment2[0], segment2[1]

    intersect = (a1 <= a2 <= b1) or\
                (a2 <= a1 <= b2)

    return intersect


def validate_input(G: Callable, u: Callable, S0: np.array, T: float,
                   Lr0_list: np.array, xl0_list: np.array, Yrl0_list: np.array,
                   LrG_list: np.array, slG_list: np.array, YrlG_list: np.array,
                   v_0: Callable, v_G: Callable) -> None:
    """

    :param G: function of two variables x, t - Green's function
    :param u: function of two variables x, t - Disturbance
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]]) - Space-time domain
    :param T: float greater that zero - Max time value
    :param Lr0_list: list of Lr0 differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param xl0_list: list of float xl0: [x0, x1, x2, ...]
    :param Yrl0_list: np.array of np.arrays of Yrl0 that is float: [[Y110, Y120, ...], ...]
    :param LrG_list: list of LrG differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param slG_list: list of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :param YrlG_list: np.array of np.arrays of YrlG that is float: [[Y11G, Y12G, ...], ...]
    :param v_0: function of two variables x, t
    :param v_G: function of two variables x, t
    :return: tuple of function of 2 variables x, t and float precision
    """
    try:
        # All data has needed type and format because they went through parser and it would have caught such problems
        for segment in S0:
            if segment[1] <= segment[0]:
                raise Exception("In S0 should be: bi > ai for all i")

        for i in range(len(S0)):
            for j in range(i + 1, len(S0)):
                if segments_intersect(S0[i], S0[j]):
                    raise Exception("Segments in S0 should not intersect")

        if T <= 0:
            raise Exception("T should be positive float")

        R0 = len(Lr0_list)
        L0 = len(xl0_list)
        if len(Yrl0_list) != R0:
            raise Exception("Counts of Lr0 and Yrl0 should match")
        for row in Yrl0_list:
            if len(row) != L0:
                raise Exception("Counts of xl0 and Yrl0 should match")

        RG = len(LrG_list)
        LG = len(slG_list)
        if len(YrlG_list) != RG:
            raise Exception("Counts of LrG and YrlG should match")
        for row in YrlG_list:
            if len(row) != LG:
                raise Exception("Counts of slG and YrlG should match")

        # There also should be validation of G but it is very hard to implement

    except Exception as e:
        raise e
