from controller import view_data_to_file, retrieve_data_from_file, validate_input
from parsings import parse_data
from calculations import solve, calculate_for_plot
from utils import beep
from datetime import datetime
import logging


def control(view, file_path: str) -> None:
    """

    :param view: object of View class
    :param file_path: string with path to the file with data
    :return: None
    """
    try:
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

        solutions = []

        for v_index in range(len(parsed_data['v0_list'])):
            solution, precision, Yrl0 = solve(parsed_data['G'], parsed_data['u'], parsed_data['S'], parsed_data['S0'], parsed_data['SG'], parsed_data['T'],
                                              parsed_data['Lr0_list'], parsed_data['xl0_list'],
                                              parsed_data['LrG_list'], parsed_data['slG_list'], parsed_data['YrlG_list'],
                                              parsed_data['Li_list'], parsed_data['sij_list'], parsed_data['Yij_list'],
                                              parsed_data['v0_list'][v_index], parsed_data['vG_list'][v_index],
                                              parsed_data['integrals_precision'])
            solution_plot_data = calculate_for_plot(
                solution, parsed_data['plot_grid_dimension'], parsed_data['X0'], parsed_data['X1'], parsed_data['T0'], parsed_data['T1'])

            solutions.append({"solution": solution, "solution_plot_data": solution_plot_data,
                              "precision": precision, "Yrl0": Yrl0})

            logging.info('Desired conditions check:')
            for i in range(len(parsed_data['Li_list'])):
                Li = parsed_data['Li_list'][i]
                for j in range(len(parsed_data['sij_list'][i])):
                    sij = parsed_data['sij_list'][i][j]
                    str_to_log = f"s{i+1}{j+1}: {sij}, Y{i+1}{j+1}: {Li(solution)(sij[0], sij[1])}"
                    logging.info(str_to_log)

        view.results_output.receive_data_and_show_it(solutions)

        end_time = datetime.now()

        # End of solving
        logging.info(f'Time to get result: {end_time - start_time}')
        beep()
    except Exception as e:
        raise e
