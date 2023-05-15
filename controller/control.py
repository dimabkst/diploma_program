import logging
from controller import view_data_to_file, retrieve_data_from_file, validate_input
from parsings import parse_data
from calculations import solve, calculate_for_plot, calculate_for_desired_values_plot, Yij, discrete_u_f, calculate_for_plot_stock_problem_transform, calculate_for_plot_stock_problem, calculate_for_desired_values_plot_stock_problem
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
        start_time = datetime.now()

        view_data_to_file(view, file_path)

        data_from_file = retrieve_data_from_file(file_path)

        parsed_data = parse_data(data_from_file, plot_stock)

        validate_input(parsed_data)

        solutions = []
        for v_index in range(len(parsed_data['v0_list'])):
            # Solution
            solution, precision, Yrl0 = solve(parsed_data['G'], parsed_data['u'], parsed_data['S'], parsed_data['S0'], parsed_data['SG'], parsed_data['T'],
                                              parsed_data['Lr0_list'], parsed_data['xl0_list'],
                                              parsed_data['LrG_list'], parsed_data['slG_list'], parsed_data['YrlG_list'],
                                              parsed_data['Li_list'], parsed_data['sij_list'], parsed_data['Yij_list'],
                                              parsed_data['v0_list'][v_index], parsed_data['vG_list'][v_index],
                                              parsed_data['integrals_precision'])

            # Plot data
            solution_plot_data, stock_problem_solution_plot_data = plot_data(
                solution, parsed_data, plot, plot_stock)

            solutions.append({"solution": solution, "solution_plot_data": solution_plot_data,
                              "precision": precision, "Yrl0": Yrl0, "stock_problem_solution_plot_data": stock_problem_solution_plot_data})

            # Log real_Yij, real_uk
            real_Yij = Yij(
                solution, parsed_data['Li_list'], parsed_data['sij_list'])

            real_uk = [discrete_u_f(real_Yij[0][k], parsed_data['stock_problem']['tk_list'][k], parsed_data['stock_problem']['gamma'])
                       for k in range(parsed_data['stock_problem']['K'])] if plot_stock else None

            log_step_info(parsed_data, real_Yij, real_uk)

        # Show results
        view.results_output.receive_data_and_show_it(solutions)

        end_time = datetime.now()

        # End of solving
        logging.info(f'Time to get result: {end_time - start_time}')
        beep()
    except Exception as e:
        raise e


def plot_data(solution, parsed_data, plot: bool, plot_stock: bool):
    try:
        solution_plot_data = None
        if plot:
            solution_plot_data = calculate_for_plot(
                solution, parsed_data['plot_grid_dimension'], parsed_data['X0'], parsed_data['X1'], parsed_data['T0'], parsed_data['T1'])

            solution_plot_data['desired_values'] = calculate_for_desired_values_plot(
                parsed_data['sij_list'], parsed_data['Yij_list'])

        stock_problem_solution_plot_data = None
        if plot_stock:
            if plot:
                # Save time by not recalculating y
                stock_problem_solution_plot_data = calculate_for_plot_stock_problem_transform(
                    solution_plot_data, parsed_data['stock_problem']['alpha'], parsed_data['stock_problem']['beta'], parsed_data['stock_problem']['gamma'])
            else:
                stock_problem_solution_plot_data = calculate_for_plot_stock_problem(
                    solution,
                    parsed_data['plot_grid_dimension'], parsed_data['X0'], parsed_data['X1'], parsed_data['T0'], parsed_data['T1'],
                    parsed_data['stock_problem']['alpha'], parsed_data['stock_problem']['beta'], parsed_data['stock_problem']['gamma'])

            stock_problem_solution_plot_data['desired_values'] = calculate_for_desired_values_plot_stock_problem(
                parsed_data['stock_problem']['xk_list'], parsed_data['stock_problem']['tk_list'], parsed_data['stock_problem']['uk_list'])

        return solution_plot_data, stock_problem_solution_plot_data
    except Exception as e:
        raise e


def log_step_info(parsed_data, real_Yij=None, real_uk=None):
    try:
        if real_Yij is not None and len(real_Yij):
            _log_real_Yij(real_Yij, parsed_data['sij_list'])

        if real_uk is not None and len(real_uk):
            _log_real_uk(
                real_uk, parsed_data['stock_problem']['xk_list'], parsed_data['stock_problem']['tk_list'])

    except Exception as e:
        raise e


def _log_real_Yij(real_Yij, sij_list):
    try:
        logging.info('Real desired conditions:')
        for i in range(len(real_Yij)):
            for j in range(len(real_Yij[i])):
                sij = sij_list[i][j]
                str_to_log = f"s{i+1}{j+1}: {sij}, Y{i+1}{j+1}: {real_Yij[i][j]}"
                logging.info(str_to_log)
    except Exception as e:
        raise e


def _log_real_uk(real_uk, xk_list, tk_list):
    try:
        logging.info('Real stock problem desired conditions:')
        for k in range(len(real_uk)):
            xk = xk_list[k]
            tk = tk_list[k]
            stock_str_to_log = f"x{k+1}: {xk}, t{k+1}: {tk}, u{k+1}: {real_uk[k]}"
            logging.info(stock_str_to_log)

    except Exception as e:
        raise e
