from numpy import array
from parsings import parse_number, parse_S_, parse_function, parse_operator, parse_slG, parse_sij, parse_stock_problem


def _parse_data(data: dict) -> dict:
    """

    :param data: dict with data retrieved from file
    :return: dict with parsed data
    """
    try:
        parsed_data = dict()

        # parse problem conditions
        parsed_data['S'] = parse_S_(data['S'])
        parsed_data['S0'] = parse_S_(data['S0'])
        parsed_data['SG'] = parse_S_(data['SG'])
        parsed_data['T'] = parse_number(data['T'])
        parsed_data['L'] = parse_operator(data['L'])
        parsed_data['u'] = parse_function(data['u'])
        parsed_data['G'] = parse_function(data['G'])

        # parse initial conditions
        parsed_data['R0'] = parse_number(data['R0'])
        parsed_data['L0'] = parse_number(data['L0'])

        parsed_data['Lr0_list'] = []
        for i in range(len(data['Lr0_list'])):
            parsed_data['Lr0_list'].append(parse_operator(data['Lr0_list'][i]))
        parsed_data['Lr0_list'] = array(parsed_data['Lr0_list'])

        parsed_data['xl0_list'] = []
        for i in range(len(data['xl0_list'])):
            parsed_data['xl0_list'].append(parse_number(data['xl0_list'][i]))
        parsed_data['xl0_list'] = array(parsed_data['xl0_list'])

        # parse boundary conditions
        parsed_data['RG'] = parse_number(data['RG'])
        parsed_data['LG'] = parse_number(data['LG'])

        parsed_data['LrG_list'] = []
        for i in range(len(data['LrG_list'])):
            parsed_data['LrG_list'].append(parse_operator(data['LrG_list'][i]))
        parsed_data['LrG_list'] = array(parsed_data['LrG_list'])

        parsed_data['slG_list'] = []
        for i in range(len(data['slG_list'])):
            parsed_data['slG_list'].append(parse_slG(data['slG_list'][i]))
        parsed_data['slG_list'] = array(parsed_data['slG_list'])

        parsed_data['YrlG_list'] = []
        for i in range(len(data['YrlG_list'])):
            parsed_data['YrlG_list'].append([])
            for ii in range(len(data['YrlG_list'][i])):
                parsed_data['YrlG_list'][-1].append(
                    parse_number(data['YrlG_list'][i][ii]))
        parsed_data['YrlG_list'] = array(parsed_data['YrlG_list'])

        # parse desired conditions
        parsed_data['I'] = parse_number(data['I'])
        parsed_data['Ji_list'] = []
        for i in range(len(data['Ji_list'])):
            parsed_data['Ji_list'].append(parse_number(data['Ji_list'][i]))
        parsed_data['Ji_list'] = array(parsed_data['Ji_list'])

        parsed_data['Li_list'] = []
        for i in range(len(data['Li_list'])):
            parsed_data['Li_list'].append(parse_operator(data['Li_list'][i]))
        parsed_data['Li_list'] = array(parsed_data['Li_list'])

        parsed_data['sij_list'] = []
        for i in range(len(data['sij_list'])):
            parsed_data['sij_list'].append([])
            for ii in range(len(data['sij_list'][i])):
                parsed_data['sij_list'][-1].append(
                    parse_sij(data['sij_list'][i][ii]))
            parsed_data['sij_list'][-1] = array(parsed_data['sij_list'][-1])
        parsed_data['sij_list'] = array(
            parsed_data['sij_list'], dtype=object)

        parsed_data['Yij_list'] = []
        for i in range(len(data['Yij_list'])):
            parsed_data['Yij_list'].append([])
            for ii in range(len(data['Yij_list'][i])):
                parsed_data['Yij_list'][-1].append(
                    parse_number(data['Yij_list'][i][ii]))
        parsed_data['Yij_list'] = array(
            parsed_data['Yij_list'], dtype=object)

        # parse v0, vG
        parsed_data['v0_list'] = []
        for i in range(len(data['v0_list'])):
            parsed_data['v0_list'].append(parse_function(data['v0_list'][i]))

        parsed_data['vG_list'] = []
        for i in range(len(data['vG_list'])):
            parsed_data['vG_list'].append(parse_function(data['vG_list'][i]))

        # parse settings
        parsed_data['integrals_precision'] = parse_number(
            data['integrals_precision'])
        parsed_data['plot_grid_dimension'] = parse_number(
            data['plot_grid_dimension'])

        parsed_data['X0'] = parse_number(data['X0'])
        parsed_data['X1'] = parse_number(data['X1'])
        parsed_data['T0'] = parse_number(data['T0'])
        parsed_data['T1'] = parse_number(data['T1'])

        return parsed_data
    except Exception as e:
        raise e


def parse_data(data: dict, stock_problem: bool):
    """

    :param data: dict with data retrieved from file
    :return: dict with parsed data
    """
    try:
        parsed_data = _parse_data(data)

        parsed_data['stock_problem'] = None
        if stock_problem:
            stock_problem_data = data['stock_problem']

            stock_problem_parsed_data = parse_stock_problem(
                stock_problem_data)

            parsed_data['stock_problem'] = stock_problem_parsed_data

        return parsed_data
    except Exception as e:
        raise e
