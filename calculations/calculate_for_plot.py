from typing import Callable, Dict
import numpy as np
import inspect


def calculate_for_plot(y_solution: Callable, count: int, A: float, B: float, T0: float, T: float) -> Dict[str, np.array]:
    try:
        if count < 1:
            raise Exception(
                f'count should be greater than 1 in {inspect.currentframe().f_code.co_name}')

        if (A > B):
            raise Exception(
                f'A should be no greater than B in {inspect.currentframe().f_code.co_name}')

        if (T0 > T):
            raise Exception(
                f'T0 should be no greater than T in {inspect.currentframe().f_code.co_name}')

        t_step = (T - T0) / (count - 1)
        x_step = (B - A) / (count - 1)

        t_values = np.arange(T0, T, t_step)
        x_values = np.arange(A, B, x_step)

        X_values, T_values = np.meshgrid(x_values, t_values)
        Y_values = [[y_solution(x_value, t_value)
                    for x_value in x_values] for t_value in t_values]
        Y_values = np.array(Y_values)

        return {'X': X_values, 'T': T_values, 'Y': Y_values}

    except Exception as e:
        raise e
