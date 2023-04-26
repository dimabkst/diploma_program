from controller import view_data_to_file, retrieve_data_from_file
from parsings import parse_data
from calculations import solve


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

        if len(parsed_data['v0_list']) != len(parsed_data['vG_list']):
            raise Exception("Lengths of v0s and vGs should be equal")
        solutions = []
        for v_index in range(len(parsed_data['v0_list'])):
            solution, precision = solve(parsed_data['G'], parsed_data['u'], parsed_data['S0'], parsed_data['SG'], parsed_data['T'],
                                        parsed_data['LrG_list'], parsed_data['slG_list'], parsed_data['YrlG_list'],
                                        parsed_data['Li_list'], parsed_data['sij_list'], parsed_data['Yij_list'],
                                        parsed_data['v0_list'][v_index], parsed_data['vG_list'][v_index])

            solutions.append({"solution": solution, "precision": precision})

            # print(f'№{v_index}. Solution: {solution}, precision: {precision}')

        S0 = sorted(parsed_data['S0'])
        dimensions = {'A': S0[0][0], 'B': S0[-1][1], 'T': parsed_data['T']}

        view.results_output.receive_data_and_show_it(solutions, dimensions)

    except Exception as e:
        raise e
