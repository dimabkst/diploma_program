from typing import Dict


def view_alpha_beta_gamma_data(view) -> Dict[str, float]:
    """

    :param view: object of View class from which to load
    :return: dit with retrieved data
    """
    try:
        alpha_beta_gamma_window = view.stock_problem_page.alpha_beta_gamma_window

        data = dict()

        data['mu'] = alpha_beta_gamma_window.mu_var.get()
        data['sigma'] = alpha_beta_gamma_window.sigma_var.get()
        data['b'] = alpha_beta_gamma_window.b_var.get()
        data['c'] = alpha_beta_gamma_window.c_var.get()

        return data
    except Exception as e:
        raise e
