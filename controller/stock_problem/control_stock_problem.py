from controller.stock_problem import view_stock_problem_data, validate_stock_problem_input, stock_problem_data_to_view
from parsings import parse_stock_problem
from calculations import transform_stocks_problem


def control_stock_problem(view) -> None:
    """

    :param view: object of View class
    :return: None
    """
    try:
        data_from_view = view_stock_problem_data(view)

        parsed_data = parse_stock_problem(data_from_view)

        validate_stock_problem_input(
            parsed_data['alpha'], parsed_data['beta'], parsed_data['gamma'],
            parsed_data['a'], parsed_data['b'], parsed_data['T'],
            parsed_data['I'], parsed_data['xi_list'],
            parsed_data['J'], parsed_data['tj_list'],
            parsed_data['K'], parsed_data['xk_list'], parsed_data['tk_list'], parsed_data['uk_list'])

        transformed_stock_problem_data = transform_stocks_problem(
            parsed_data['alpha'], parsed_data['beta'], parsed_data['gamma'],
            parsed_data['a'], parsed_data['b'], parsed_data['T'],
            parsed_data['I'], parsed_data['xi_list'],
            parsed_data['J'], parsed_data['tj_list'],
            parsed_data['K'], parsed_data['xk_list'], parsed_data['tk_list'], parsed_data['uk_list'])

        stock_problem_data_to_view(view, transformed_stock_problem_data)

    except Exception as e:
        raise e
