from controller import retrieve_data_from_file
from tkinter import StringVar


def file_data_to_view(view, file_path: str) -> None:
    """

    :param view: object of View class in which to save
    :param file_path: string with path to the file from which to load
    :return: None
    """
    try:
        problem_conditions_input = view.problem_conditions_input
        initial_conditions_input = view.initial_boundary_conditions_input.initial_conditions_input
        boundary_conditions_input = view.initial_boundary_conditions_input.boundary_conditions_input
        v_input = view.v_input

        # reading json file
        data = retrieve_data_from_file(file_path)

        # problem conditions
        problem_conditions_input.S0_var.set(data['S0'])
        problem_conditions_input.T_var.set(data['T'])
        problem_conditions_input.L_var.set(data['L'])
        problem_conditions_input.u_var.set(data['u'])
        problem_conditions_input.G_var.set(data['G'])

        # initial conditions
        initial_conditions_input.R0_var.set(data['R0'])
        initial_conditions_input.change_and_show_initial()
        for _ in range(len(data['Lr0_list'])):
            initial_conditions_input.Lr0_vars[-1].set(data['Lr0_list'][_])

        initial_conditions_input.L0_var.set(data['L0'])
        initial_conditions_input.change_and_show_initial()
        for _ in range(len(data['xl0_list'])):
            initial_conditions_input.xl0_vars[-1].set(data['xl0_list'][_])

        for _ in range(len(data['Yrl0_list'])):
            for __ in range(len(data['Yrl0_list'][_])):
                initial_conditions_input.yrl0_vars[-1][-1].set(data['Yrl0_list'][_][__])

        # boundary conditions
        boundary_conditions_input.RG_var.set(data['RG'])
        boundary_conditions_input.change_and_show_boundary()
        for _ in range(len(data['LrG_list'])):
            boundary_conditions_input.LrG_vars[-1].set(data['LrG_list'][_])

        boundary_conditions_input.LG_var.set(data['LG'])
        boundary_conditions_input.change_and_show_boundary()
        for _ in range(len(data['slG_list'])):
            boundary_conditions_input.slG_vars[-1].set(data['slG_list'][_])

        for _ in range(len(data['YrlG_list'])):
            for __ in range(len(data['YrlG_list'][_])):
                boundary_conditions_input.yrlG_vars[-1][-1].set(data['YrlG_list'][_][__])

        # v
        v_input.count_var.set(len(data['v0_list']))
        v_input.change_and_show_v()

        for _ in range(len(data['v0_list'])):
            v_input.v0_vars[-1].set(data['v0_list'][_])

        for _ in range(len(data['vG_list'])):
            v_input.vG_vars[-1].set(data['vG_list'][_])

    except Exception as e:
        raise e
