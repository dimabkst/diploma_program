import logging
from controller import view_data_to_file, retrieve_data_from_file, validate_input, validate_stock_problem_input
from parsings import parse_data, parse_stock_problem
from calculations import solve, calculate_for_plot, Yij, discrete_u_f, calculate_for_plot_stock_problem_transform
from utils import beep
from datetime import datetime


def control(view, file_path: str, plot: bool, plot_stock: bool) -> None:
    """

    :param view: object of View class
    :param file_path: string with path to the file with data
    :param plot_stock: plot solutions for stock prtoblem or not
    :return: None
    """
    try:
        if plot_stock and not plot:
            raise Exception(
                'For now you cannot plot stock problem without plot problem')

        start_time = datetime.now()

        view_data_to_file(view, file_path)

        data_from_file = retrieve_data_from_file(file_path)

        parsed_data = parse_data(data_from_file)

        validate_input(parsed_data['G'], parsed_data['u'], parsed_data['S'], parsed_data['S0'], parsed_data['SG'], parsed_data['T'],
                       parsed_data['Lr0_list'], parsed_data['xl0_list'],
                       parsed_data['LrG_list'], parsed_data['slG_list'], parsed_data['YrlG_list'],
                       parsed_data['Li_list'], parsed_data['sij_list'], parsed_data['Yij_list'],
                       parsed_data['v0_list'], parsed_data['vG_list'],
                       parsed_data['integrals_precision'], parsed_data['plot_grid_dimension'],
                       parsed_data['X0'], parsed_data['X1'], parsed_data['T0'], parsed_data['T1'])

        if plot_stock:
            stock_problem_data_from_view = data_from_file['stock_problem']

            stock_problem_parsed_data = parse_stock_problem(
                stock_problem_data_from_view)

            validate_stock_problem_input(
                stock_problem_parsed_data['alpha'], stock_problem_parsed_data['beta'], stock_problem_parsed_data['gamma'],
                stock_problem_parsed_data['a'], stock_problem_parsed_data['b'], stock_problem_parsed_data['T'],
                stock_problem_parsed_data['I'], stock_problem_parsed_data['xi_list'],
                stock_problem_parsed_data['J'], stock_problem_parsed_data['tj_list'],
                stock_problem_parsed_data['K'], stock_problem_parsed_data['xk_list'], stock_problem_parsed_data['tk_list'], stock_problem_parsed_data['uk_list'])

            parsed_data['stock_problem'] = stock_problem_parsed_data

        solutions = []

        for v_index in range(len(parsed_data['v0_list'])):
            solution, precision, Yrl0 = solve(parsed_data['G'], parsed_data['u'], parsed_data['S'], parsed_data['S0'], parsed_data['SG'], parsed_data['T'],
                                              parsed_data['Lr0_list'], parsed_data['xl0_list'],
                                              parsed_data['LrG_list'], parsed_data['slG_list'], parsed_data['YrlG_list'],
                                              parsed_data['Li_list'], parsed_data['sij_list'], parsed_data['Yij_list'],
                                              parsed_data['v0_list'][v_index], parsed_data['vG_list'][v_index],
                                              parsed_data['integrals_precision'])

            solution_plot_data = calculate_for_plot(
                solution, parsed_data['plot_grid_dimension'], parsed_data['X0'], parsed_data['X1'], parsed_data['T0'], parsed_data['T1']) if plot else None
            stock_problem_solution_plot_data = calculate_for_plot_stock_problem_transform(
                solution_plot_data, parsed_data['stock_problem']['alpha'], parsed_data['stock_problem']['beta'], parsed_data['stock_problem']['gamma']) if plot_stock else None

            solutions.append({"solution": solution, "solution_plot_data": solution_plot_data,
                              "precision": precision, "Yrl0": Yrl0, "stock_problem_solution_plot_data": stock_problem_solution_plot_data})

            logging.info('Real desired conditions:')
            real_Yij = Yij(
                solution, parsed_data['Li_list'], parsed_data['sij_list'])
            for i in range(len(real_Yij)):
                for j in range(len(real_Yij[i])):
                    sij = parsed_data['sij_list'][i][j]
                    str_to_log = f"s{i+1}{j+1}: {sij}, Y{i+1}{j+1}: {real_Yij[i][j]}"
                    logging.info(str_to_log)

            if plot_stock:
                logging.info('Real stock problem desired conditions:')
                real_uk = [discrete_u_f(real_Yij[0][k], parsed_data['stock_problem']['tk_list'][k], parsed_data['stock_problem']['gamma'])
                           for k in range(parsed_data['stock_problem']['K'])]
                for k in range(len(real_uk)):
                    xk = parsed_data['stock_problem']['xk_list'][k]
                    tk = parsed_data['stock_problem']['tk_list'][k]
                    stock_str_to_log = f"x{k+1}: {xk}, t{k+1}: {tk}, u{k+1}: {real_uk[k]}"
                    logging.info(stock_str_to_log)

        view.results_output.receive_data_and_show_it(solutions)

        end_time = datetime.now()

        # End of solving
        logging.info(f'Time to get result: {end_time - start_time}')
        beep()
    except Exception as e:
        raise e
