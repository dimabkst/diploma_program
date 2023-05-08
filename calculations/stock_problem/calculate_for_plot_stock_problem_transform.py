from typing import Dict
import numpy as np
from calculations.stock_problem import x_f, t_f, discrete_u_f, C_f


def calculate_for_plot_stock_problem_transform(data: Dict[str, np.array], alpha: float, beta: float, gamma: float) -> Dict[str, np.array]:
    try:
        T_values = np.array([[t_f(data['T'][i][j], alpha) for j in range(
            len(data['T'][i]))] for i in range(len(data['T']))])

        X_values = np.array([[x_f(data['X'][i][j], data['T'][i][j], C_f(alpha, beta), alpha) for j in range(
            len(data['X'][i]))] for i in range(len(data['X']))])

        Y_values = np.array([[discrete_u_f(data['Y'][i][j], T_values[i][j], gamma) for j in range(
            len(data['Y'][i]))] for i in range(len(data['Y']))])

        return {'X': X_values, 'T': T_values, 'Y': Y_values}
    except Exception as e:
        raise e
