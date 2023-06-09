from numpy import array
from typing import Callable, Tuple
from calculations import y_infinity, A, Y_slash, A_v, P, u_0G, y_0, y_G, y, precision, Yrl0


def solve(G: Callable, u: Callable, S: array, S0: array, SG: array, T: float,
          Lr0_list: array, xl0_list: array,
          LrG_list: array, slG_list: array, YrlG_list: array,
          Li_list: array, sij_list: array, Yij_list: array,
          v_0: Callable, v_G: Callable,
          integrals_precision: float) -> Tuple[Callable, float, array]:
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
    :param integrals_precision: dblquad integrals precision
    :return: tuple of function of 2 variables x, t, float precision and np.array of np.arrays with floats
    """
    try:
        # In S0 should be b1 < a2 etc
        S.sort()
        S0.sort()
        SG.sort()

        res_y_infinity = y_infinity(G, u, S, T, integrals_precision)
        res_A = A(G, LrG_list, slG_list, Li_list, sij_list)
        res_Y_slash = Y_slash(res_y_infinity,
                              LrG_list, slG_list, YrlG_list, Li_list, sij_list, Yij_list)
        res_A_v = A_v(res_A, v_0, v_G, S0, SG, T, integrals_precision)
        res_P = P(res_A, S0, SG, T, integrals_precision)
        res_u_0, res_u_G = u_0G(res_A, res_P, res_Y_slash, res_A_v, v_0, v_G)
        res_y_0 = y_0(G, S0, T, res_u_0, integrals_precision)
        res_y_G = y_G(G, SG, T, res_u_G, integrals_precision)
        res_y = y(res_y_infinity, res_y_0, res_y_G)

        res_precision = precision(res_Y_slash, res_P)

        res_Yrl0 = Yrl0(res_y, Lr0_list, xl0_list)

        return res_y, res_precision, res_Yrl0
    except Exception as e:
        raise e
