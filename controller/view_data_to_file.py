from controller import put_data_to_file


def view_data_to_file(view, file_path: str) -> None:
    """

    :param view: object of View class from which to load
    :param file_path: string with path to the file in which to save
    :return: None
    """
    try:
        problem_conditions_input = view.problem_conditions_input
        boundary_conditions_input = view.boundary_desired_conditions_input.boundary_conditions_input
        desired_conditions_input = view.boundary_desired_conditions_input.desired_conditions_input
        v_input = view.v_input

        data = dict()

        # problem conditions
        data['S0'] = problem_conditions_input.S0_var.get()
        data['SG'] = problem_conditions_input.SG_var.get()
        data['T'] = problem_conditions_input.T_var.get()
        data['L'] = problem_conditions_input.L_var.get()
        data['u'] = problem_conditions_input.u_var.get()
        data['G'] = problem_conditions_input.G_var.get()

        # boundary conditions
        data['RG'] = boundary_conditions_input.RG_var.get()
        data['LrG_list'] = []
        for _ in range(len(boundary_conditions_input.LrG_vars)):
            data['LrG_list'].append(
                boundary_conditions_input.LrG_vars[_].get())

        data['LG'] = boundary_conditions_input.LG_var.get()
        data['slG_list'] = []
        for _ in range(len(boundary_conditions_input.slG_vars)):
            data['slG_list'].append(
                boundary_conditions_input.slG_vars[_].get())

        data['YrlG_list'] = []
        for _ in range(len(boundary_conditions_input.LrG_vars)):
            data['YrlG_list'].append([])
            for __ in range(len(boundary_conditions_input.slG_vars)):
                data['YrlG_list'][-1].append(
                    boundary_conditions_input.yrlG_vars[_][__].get())

        # desired conditions
        data['I'] = desired_conditions_input.I_var.get()
        data['Li_list'] = []
        for _ in range(len(desired_conditions_input.Li_vars)):
            data['Li_list'].append(desired_conditions_input.Li_vars[_].get())

        data['Ji_list'] = []
        for _ in range(len(desired_conditions_input.Ji_vars)):
            data['Ji_list'].append(desired_conditions_input.Ji_vars[_].get())

        data['sij_list'] = []
        for _ in range(len(desired_conditions_input.sij_vars)):
            data['sij_list'].append([])
            for __ in range(len(desired_conditions_input.sij_vars[_])):
                data['sij_list'][-1].append(
                    desired_conditions_input.sij_vars[_][__].get())

        data['Yij_list'] = []
        for _ in range(len(desired_conditions_input.yij_vars)):
            data['Yij_list'].append([])
            for __ in range(len(desired_conditions_input.yij_vars[_])):
                data['Yij_list'][-1].append(
                    desired_conditions_input.yij_vars[_][__].get())

        # v
        data['v0_list'] = []
        for _ in range(len(v_input.v0_vars)):
            data['v0_list'].append(v_input.v0_vars[_].get())

        data['vG_list'] = []
        for _ in range(len(v_input.vG_vars)):
            data['vG_list'].append(v_input.vG_vars[_].get())

        # saving in json file
        put_data_to_file(file_path, data)

    except Exception as e:
        raise e
