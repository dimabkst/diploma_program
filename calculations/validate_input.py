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


def validate_input(G: Callable, u: Callable, S0: np.array, SG: np.array, T: float,
                   LrG_list: np.array, slG_list: np.array, YrlG_list: np.array,
                   Li_list: np.array, sij_list: np.array, Yij_list: np.array,
                   v_0: Callable, v_G: Callable) -> None:
    """

    :param G: function of two variables x, t - Green's function
    :param u: function of two variables x, t - Disturbance
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]]) - Space domain
    :param SG: has next form: np.array([[c0, d0],...,[c_last, d_last]]) - Boundary space domain
    :param T: float greater that zero - Max time value
    :param LrG_list: list of LrG differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param slG_list: list of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :param YrlG_list: np.array of np.arrays of YrlG that is float: [[Y11G, Y12G, ...], ...]
    :param Li_list: list of Li differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param sij_list: np.array of np.arrays of of sij that is np.array of two float values x and t: [[[x00, t00], [x01, t01], ...], ...]
    :param Yij_list: np.array of np.arrays of Yij that is float: [[Y11, Y12, ...], ...]
    :param v_0: function of two variables x, t
    :param v_G: function of two variables x, t
    :return: tuple of function of 2 variables x, t and float precision
    """
    try:
        # All data has needed type and format because they went through parser and it would have caught such problems
        for segment in S0:
            if segment[1] <= segment[0]:
                raise Exception("In S0 should be: bk > ak for all k")

        for i in range(len(S0)):
            for j in range(i + 1, len(S0)):
                if segments_intersect(S0[i], S0[j]):
                    raise Exception("Segments in S0 should not intersect")

        for segment in SG:
            if segment[1] <= segment[0]:
                raise Exception("In SG should be: de > ce for all e")

        for i in range(len(SG)):
            for j in range(i + 1, len(SG)):
                if segments_intersect(SG[i], SG[j]):
                    raise Exception("Segments in SG should not intersect")

        if T <= 0:
            raise Exception("T should be positive float")

        I = len(Li_list)
        if len(Yij_list) != I:
            raise Exception("Counts of Li and Yij should match")
        for row in Yij_list:
            if len(row) != len(sij_list):
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
