import numpy as np
import inspect
from typing import Callable, Dict
from calculations.stock_problem import C_f, x_f, t_f, u_f


def calculate_for_plot_stock_problem(y_solution: Callable, count: int, Z0: float, Z1: float, TAU0: float, TAU1: float, alpha: float, beta: float, gamma: float) -> Dict[str, np.array]:
    """

    :param y_solution: function of two variables z, tau
    :param count: count of points where to calculate function on each axis 
    :param Z0: start point on z axis
    :param Z1: end point on z axis
    :param T0: start point on tau axis
    :param T: end point on tau axis
    :return: dict of points on axes and values of function to plot
    """

    try:
        if count < 1:
            raise Exception(
                f'count should be greater than 1 in {inspect.currentframe().f_code.co_name}')

        if (Z0 > Z1):
            raise Exception(
                f'Z0 should be no greater than Z1 in {inspect.currentframe().f_code.co_name}')

        if (TAU0 > TAU1):
            raise Exception(
                f'TAU0 should be no greater than TAU1 in {inspect.currentframe().f_code.co_name}')

        X0 = x_f(Z0, TAU0, C_f(alpha, beta), alpha)
        X1 = x_f(Z1, TAU1, C_f(alpha, beta), alpha)

        T0 = t_f(TAU0, alpha)
        T1 = t_f(TAU1, alpha)

        t_values = np.linspace(T0, T1, count)
        x_values = np.linspace(X0, X1, count)

        u_solution = u_f(y_solution, alpha, beta, gamma)

        X_values, T_values = np.meshgrid(x_values, t_values)
        Y_values = [[u_solution(x_value, t_value)
                    for x_value in x_values] for t_value in t_values]
        Y_values = np.array(Y_values)

        return {'X': X_values, 'T': T_values, 'Y': Y_values}

    except Exception as e:
        raise e
