from typing import Dict


def alpha_beta_gamma_data_to_view(view, data: Dict[str, float]) -> None:
    """

    :param view: object of View class in which to save
    :param data: data to put im view
    :return: None
    """
    try:
        alpha_beta_gamma_window = view.stock_problem_page.alpha_beta_gamma_window
        stock_problem_window = view.stock_problem_page.stock_problem_window

        alpha_beta_gamma_window.alpha_var.set(data['alpha'])
        alpha_beta_gamma_window.beta_var.set(data['beta'])
        alpha_beta_gamma_window.gamma_var.set(data['gamma'])

        stock_problem_window.alpha_var.set(data['alpha'])
        stock_problem_window.beta_var.set(data['beta'])
        stock_problem_window.gamma_var.set(data['gamma'])

    except Exception as e:
        raise e
