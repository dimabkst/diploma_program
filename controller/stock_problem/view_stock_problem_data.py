from typing import Dict


def view_stock_problem_data(view) -> Dict[str, float]:
    """

    :param view: object of View class from which to load
    :return: dit with retrieved data
    """
    try:
        stock_problem_window = view.stock_problem_page.stock_problem_window

        data = dict()

        data['alpha'] = stock_problem_window.alpha_var.get()
        data['beta'] = stock_problem_window.beta_var.get()
        data['gamma'] = stock_problem_window.gamma_var.get()
        data['a'] = stock_problem_window.a_var.get()
        data['b'] = stock_problem_window.b_var.get()
        data['T'] = stock_problem_window.T_var.get()

        # initial conditions
        data['I'] = stock_problem_window.I_var.get()
        data['xi_list'] = []
        for _ in range(len(stock_problem_window.xi_vars)):
            data['xi_list'].append(
                stock_problem_window.xi_vars[_].get())

        # boundary conditions
        data['J'] = stock_problem_window.J_var.get()
        data['tj_list'] = []
        for _ in range(len(stock_problem_window.tj_vars)):
            data['tj_list'].append(
                stock_problem_window.tj_vars[_].get())

        # desired conditions
        data['K'] = stock_problem_window.K_var.get()
        data['xk_list'] = []
        for _ in range(len(stock_problem_window.xk_vars)):
            data['xk_list'].append(
                stock_problem_window.xk_vars[_].get())
        data['tk_list'] = []
        for _ in range(len(stock_problem_window.tk_vars)):
            data['tk_list'].append(
                stock_problem_window.tk_vars[_].get())
        data['uk_list'] = []
        for _ in range(len(stock_problem_window.uk_vars)):
            data['uk_list'].append(
                stock_problem_window.uk_vars[_].get())

        return data
    except Exception as e:
        raise e
