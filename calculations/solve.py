from typing import Callable, Tuple
import numpy as np
from calculations import y_infinity, A, Y_slash, A_v, P, u_0, u_G, y_0, y_G, y, precision, validate_input


def solve(G: Callable, u: Callable, S0: np.array, SG: np.array, T: float,
          Lr0_list: np.array, xl0_list: np.array, Yrl0_list: np.array,
          LrG_list: np.array, slG_list: np.array, YrlG_list: np.array,
          Li_list: np.array, sij_list: np.array, Yij_list: np.array,
          v_0: Callable, v_G: Callable) -> Tuple[Callable, float]:
    """

    :param G: function of two variables x, t - Green's function
    :param u: function of two variables x, t - Disturbance
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]]) - Space domain
    :param SG: has next form: np.array([[c0, d0],...,[c_last, d_last]]) - Boundary space domain
    :param T: float greater that zero - Max time value
    :param Lr0_list: list of Lr0 differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param xl0_list: list of float xl0: [x0, x1, x2, ...]
    :param Yrl0_list: np.array of np.arrays of Yrl0 that is float: [[Y110, Y120, ...], ...]
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
        validate_input(G, u, S0, SG, T,
                       LrG_list, slG_list, YrlG_list,
                       Li_list, sij_list, Yij_list,
                       v_0, v_G)

        res_y_infinity = y_infinity(G, u, S0, T)
        res_A = A(G, Lr0_list, xl0_list, LrG_list, slG_list)
        res_Y_slash = Y_slash(res_y_infinity, Lr0_list,
                              xl0_list, Yrl0_list, LrG_list, slG_list, YrlG_list)
        res_A_v = A_v(res_A, v_0, v_G, S0, T)
        res_P = P(res_A, S0, T)
        res_u_0 = u_0(res_A, res_P, res_Y_slash, res_A_v, v_0)
        res_u_G = u_G(res_A, res_P, res_Y_slash, res_A_v, v_G)
        res_y_0 = y_0(G, S0, T, res_u_0)
        res_y_G = y_G(G, SG, T, res_u_G)
        res_y = y(res_y_infinity, res_y_0, res_y_G)

        res_precision = precision(res_Y_slash, res_P)

        return res_y, res_precision
    except Exception as e:
        raise e
