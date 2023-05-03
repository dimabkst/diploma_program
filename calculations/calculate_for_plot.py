from typing import Callable, Dict
import numpy as np
import inspect


def calculate_for_plot(y_solution: Callable, count: int, X0: float, X1: float, T0: float, T1: float) -> Dict[str, np.array]:
    """

    :param y_solution: function of two variables x, t to calculate for plot
    :param count: count of points where to calculate function on each axis 
    :param A: start point on x axis
    :param B: end point on x axis
    :param T0: start point on t axis
    :param T: end point on t axis
    :return: dict of points on axes and values of function to plot
    """

    try:
        if count < 1:
            raise Exception(
                f'count should be greater than 1 in {inspect.currentframe().f_code.co_name}')

        if (X0 > X1):
            raise Exception(
                f'X0 should be no greater than X1 in {inspect.currentframe().f_code.co_name}')

        if (T0 > T1):
            raise Exception(
                f'T0 should be no greater than T1 in {inspect.currentframe().f_code.co_name}')

        t_values = np.linspace(T0, T1, count)
        x_values = np.linspace(X0, X1, count)

        X_values, T_values = np.meshgrid(x_values, t_values)
        Y_values = [[y_solution(x_value, t_value)
                    for x_value in x_values] for t_value in t_values]
        Y_values = np.array(Y_values)

        return {'X': X_values, 'T': T_values, 'Y': Y_values}

    except Exception as e:
        raise e
