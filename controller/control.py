from controller import view_data_to_file, retrieve_data_from_file
from parsings import parse_data
from calculations import solve, calculate_for_plot


def control(view, file_path: str) -> None:
    """

    :param view: object of View class
    :param file_path: string with path to the file with data
    :return:
    """
    try:
        view_data_to_file(view, file_path)

        data_from_file = retrieve_data_from_file(file_path)

        parsed_data = parse_data(data_from_file)
        # print(parsed_data)

        S0 = sorted(parsed_data['S0'])
        dimensions = {'A': S0[0][0], 'B': S0[-1][1], 'T': parsed_data['T']}
        plot_count = 40 + 1  # grid for plot would be p_c * p_c

        if len(parsed_data['v0_list']) != len(parsed_data['vG_list']):
            raise Exception("Lengths of v0s and vGs should be equal")
        solutions = []
        for v_index in range(len(parsed_data['v0_list'])):
            solution, precision = solve(parsed_data['G'], parsed_data['u'], parsed_data['S0'], parsed_data['SG'], parsed_data['T'],
                                        parsed_data['LrG_list'], parsed_data['slG_list'], parsed_data['YrlG_list'],
                                        parsed_data['Li_list'], parsed_data['sij_list'], parsed_data['Yij_list'],
                                        parsed_data['v0_list'][v_index], parsed_data['vG_list'][v_index])
            solution_plot_data = calculate_for_plot(
                solution, plot_count, dimensions['A'], dimensions['B'], -dimensions['T'], dimensions['T'])

            solutions.append({"solution": solution, "solution_plot_data": solution_plot_data,
                              "precision": precision})

            # print(
            # f'№{v_index + 1}. Solution plot data: {solution_plot_data}, precision: {precision}')

        view.results_output.receive_data_and_show_it(solutions)

    except Exception as e:
        raise e
