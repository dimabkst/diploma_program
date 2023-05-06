from controller.stock_problem import view_alpha_beta_gamma_data, validate_alpha_beta_gamma_input, alpha_beta_gamma_data_to_view
from parsings import parse_alpha_beta_gamma_data
from calculations import alpha_beta_gamma


def control_alpha_beta_gamma(view) -> None:
    """

    :param view: object of View class
    :return: None
    """
    try:
        data_from_view = view_alpha_beta_gamma_data(view)

        parsed_data = parse_alpha_beta_gamma_data(data_from_view)

        validate_alpha_beta_gamma_input(
            parsed_data['mu'], parsed_data['sigma'], parsed_data['b'], parsed_data['c'])

        alpha_beta_gamma_res = alpha_beta_gamma(
            parsed_data['mu'], parsed_data['sigma'], parsed_data['b'], parsed_data['c'])

        alpha_beta_gamma_data_to_view(view, alpha_beta_gamma_res)

    except Exception as e:
        raise e
