from typing import Callable
import numpy as np


def dim1PointInSet(point: float, pointSet: np.array) -> bool:
    """

    :param point: 1 dimension point with next form: coord1 as float
    :param pointSet: set that point should be in with next form: np.array([[a0, b0],...,[a_last, b_last]])
    """

    if not (len(pointSet)):
        raise Exception(
            'Set should have form of one array whit at least one 2 dims array')

    pointInSet = False
    for i in range(len(pointSet)):
        if (len(pointSet[i]) != 2):
            raise Exception(
                'Set should be array of 2 dims arrays')

        pointInSet = pointInSet or (pointSet[i][0] <= point <= pointSet[i][1])

    return pointInSet


def dim2PointInSet(point: np.array, firstCoordSet: np.array, secondCoordSet: np.array) -> bool:
    """

    :param point: 2 dimension point with next form: np.array([coord1, coord2])
    :param firstCoordSet: set that first coord should be in with next form: np.array([[a0, b0],...,[a_last, b_last]])
    :param secondCoordSet: set that second coord should be in with next form: np.array([[c0, d0],...,[c_last, d_last]])
    """

    if len(point) != 2:
        raise Exception('Point should have 2 dimensions')
    if not (len(firstCoordSet) and len(secondCoordSet)):
        raise Exception(
            'Sets should have form of one array whit at least one 2 dims array')

    coordsInSet = [False, False]
    coordsSet = [firstCoordSet, secondCoordSet]
    for coordNumber in range(len(coordsSet)):
        coordSet = coordsSet[coordNumber]
        for i in range(len(coordSet)):
            if (len(coordSet[i]) != 2):
                raise Exception(
                    'Each coordSet should be array of 2 dims arrays')

            coordsInSet[coordNumber] = coordsInSet[coordNumber] or (
                coordSet[i][0] <= point[coordNumber] <= coordSet[i][1])

    return coordsInSet[0] and coordsInSet[1]


# Do not let segments intersect even in in boundaries,
# because do not know if integrals would be calculated correctly
def segments_intersect(segment1: np.array, segment2: np.array) -> bool:
    a1, b1 = segment1[0], segment1[1]
    a2, b2 = segment2[0], segment2[1]

    intersect = (a1 <= a2 <= b1) or\
                (a2 <= a1 <= b2)

    return intersect


def validate_input(G: Callable, u: Callable, S: np.array, S0: np.array, SG: np.array, T: float,
                   Lr0_list: np.array, xl0_list: np.array,
                   LrG_list: np.array, slG_list: np.array, YrlG_list: np.array,
                   Li_list: np.array, sij_list: np.array, Yij_list: np.array,
                   v_0: Callable, v_G: Callable) -> None:
    """

    :param G: function of two variables x, t - Green's function
    :param u: function of two variables x, t - Disturbance
    :param S: has next form: np.array([[f0, g0],...,[f_last, g_last]]) - Space domain
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]]) - Initial space domain
    :param SG: has next form: np.array([[c0, d0],...,[c_last, d_last]]) - Boundary space domain
    :param T: float greater that zero - Max time value
    :param Lr0_list: list of Lr0 differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param xl0_list: list of float xl0: [x0, x1, x2, ...]
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
        for segment in S:
            if segment[1] <= segment[0]:
                raise Exception("In S should be: bk > ak for all k")

        for i in range(len(S)):
            for j in range(i + 1, len(S)):
                if segments_intersect(S[i], S[j]):
                    raise Exception("Segments in S should not intersect")

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

        for point in xl0_list:
            if not dim1PointInSet(point, S0):
                raise Exception(f"xl0 = {point} not in {S0}")

        RG = len(LrG_list)
        LG = len(slG_list)
        if len(YrlG_list) != RG:
            raise Exception("Counts of LrG and YrlG should match")
        for row in YrlG_list:
            if len(row) != LG:
                raise Exception("Counts of slG and YrlG should match")
        for i in range(LG):
            if not dim2PointInSet(slG_list[i], SG, [[0, T]]):
                raise Exception(f"slG = {slG_list[i]} not in {SG} x {[0, T]}")

        I = len(Li_list)
        if len(Yij_list) != I:
            raise Exception("Counts of Li and rows of Yij should match")
        if len(sij_list) != I:
            raise Exception("Counts of Li and rows of sij should match")
        for i in range(len(Yij_list)):
            if len(Yij_list[i]) != len(sij_list[i]):
                raise Exception(
                    "Counts of corresponding rows of Yij and sij should match")
            for j in range(len(sij_list[i])):
                if not dim2PointInSet(sij_list[i][j], SG, [[0, T]]):
                    raise Exception(
                        f"sij = {sij_list[i][j]} not in {SG} x {[0, T]}")

        # There also should be validation of G but it is very hard to implement

    except Exception as e:
        raise e
