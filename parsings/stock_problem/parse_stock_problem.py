from parsings import parse_number


def parse_stock_problem(data: dict) -> dict:
    """

    :param data: dict with data retrieved from file
    :return: dict with parsed data
    """
    try:
        parsed_data = dict()

        # parse problem conditions
        parsed_data['alpha'] = parse_number(data['alpha'])
        parsed_data['beta'] = parse_number(data['beta'])
        parsed_data['gamma'] = parse_number(data['gamma'])
        parsed_data['a'] = parse_number(data['a'])
        parsed_data['b'] = parse_number(data['b'])
        parsed_data['T'] = parse_number(data['T'])

        # parse initial conditions
        parsed_data['I'] = parse_number(data['I'])

        parsed_data['xi_list'] = []
        for i in range(len(data['xi_list'])):
            parsed_data['xi_list'].append(parse_number(data['xi_list'][i]))

        # parse boundary conditions
        parsed_data['J'] = parse_number(data['J'])

        parsed_data['tj_list'] = []
        for i in range(len(data['tj_list'])):
            parsed_data['tj_list'].append(parse_number(data['tj_list'][i]))

        # parse desired conditions
        parsed_data['K'] = parse_number(data['K'])

        parsed_data['xk_list'] = []
        for i in range(len(data['xk_list'])):
            parsed_data['xk_list'].append(parse_number(data['xk_list'][i]))

        parsed_data['tk_list'] = []
        for i in range(len(data['tk_list'])):
            parsed_data['tk_list'].append(parse_number(data['tk_list'][i]))

        parsed_data['uk_list'] = []
        for i in range(len(data['uk_list'])):
            parsed_data['uk_list'].append(parse_number(data['uk_list'][i]))

        return parsed_data
    except Exception as e:
        raise e
