from numpy import array, linspace, meshgrid
from inspect import currentframe
from typing import Callable, Dict


def calculate_for_plot(y_solution: Callable, count: int, X0: float, X1: float, T0: float, T1: float) -> Dict[str, array]:
    """

    :param y_solution: function of two variables x, t to calculate for plot
    :param count: count of points where to calculate function on each axis 
    :param X0: start point on x axis
    :param Y0: end point on x axis
    :param T0: start point on t axis
    :param T: end point on t axis
    :return: dict of points on axes and values of function to plot
    """

    try:
        if count < 1:
            raise Exception(
                f'count should be greater than 1 in {currentframe().f_code.co_name}')

        if (X0 > X1):
            raise Exception(
                f'X0 should be no greater than X1 in {currentframe().f_code.co_name}')

        if (T0 > T1):
            raise Exception(
                f'T0 should be no greater than T1 in {currentframe().f_code.co_name}')

        t_values = linspace(T0, T1, count)
        x_values = linspace(X0, X1, count)

        X_values, T_values = meshgrid(x_values, t_values)
        Y_values = [[y_solution(x_value, t_value)
                    for x_value in x_values] for t_value in t_values]
        Y_values = array(Y_values)

        return {'X': X_values, 'T': T_values, 'Y': Y_values}

    except Exception as e:
        raise e


def calculate_for_desired_values_plot(s_values: array, y_values: array) -> Dict[str, array]:
    """

    :param s_values: np.array of np.arrays of s that is np.array of two float values x and t: [[[x00, t00], [x01, t01], ...], ...]
    :param y_values: np.array of np.arrays of y that is float: [[Y11, Y12, ...], ...]
    :return: dict of points on axes and values of dots to plot
    """

    return {'X': array([[s_values[i][j][0] for j in range(len(s_values[i]))] for i in range(len(s_values))], dtype='object').flatten(),
            'T': array([[s_values[i][j][1] for j in range(len(s_values[i]))] for i in range(len(s_values))], dtype='object').flatten(),
            'Y': y_values.flatten()}
