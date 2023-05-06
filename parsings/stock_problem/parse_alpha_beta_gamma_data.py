from parsings import parse_number


def parse_alpha_beta_gamma_data(data: dict) -> dict:
    """

    :param data: dict with data retrieved view
    :return: dict with parsed data
    """
    try:
        parsed_data = dict()

        parsed_data['mu'] = parse_number(data['mu'])
        parsed_data['sigma'] = parse_number(data['sigma'])
        parsed_data['b'] = parse_number(data['b'])
        parsed_data['c'] = parse_number(data['c'])

        return parsed_data
    except Exception as e:
        raise e
