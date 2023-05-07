from typing import Dict


def stock_problem_data_to_view(view, data: Dict[str, float]) -> None:
    """

    :param view: object of View class in which to save
    :param data: data to put im view
    :return: None
    """
    try:
        problem_conditions_input = view.problem_conditions_input
        initial_conditions_input = view.initial_boundary_desired_conditions_input.initial_conditions_input
        boundary_conditions_input = view.initial_boundary_desired_conditions_input.boundary_conditions_input
        desired_conditions_input = view.initial_boundary_desired_conditions_input.desired_conditions_input

        # problem conditions
        problem_conditions_input.S_var.set(data['S'])
        problem_conditions_input.S0_var.set(data['S0'])
        problem_conditions_input.SG_var.set(data['SG'])
        problem_conditions_input.T_var.set(data['T'])
        problem_conditions_input.L_var.set(data['L'])
        problem_conditions_input.u_var.set(data['u'])
        problem_conditions_input.G_var.set(data['G'])

        # initial conditions
        initial_conditions_input.R0_var.set(data['R0'])
        initial_conditions_input.change_and_show_initial()
        for _ in range(len(data['Lr0_list'])):
            initial_conditions_input.Lr0_vars[_].set(data['Lr0_list'][_])

        initial_conditions_input.L0_var.set(data['L0'])
        initial_conditions_input.change_and_show_initial()
        for _ in range(len(data['xl0_list'])):
            initial_conditions_input.xl0_vars[_].set(data['xl0_list'][_])

        # boundary conditions
        boundary_conditions_input.RG_var.set(data['RG'])
        boundary_conditions_input.change_and_show_boundary()
        for _ in range(len(data['LrG_list'])):
            boundary_conditions_input.LrG_vars[_].set(data['LrG_list'][_])

        boundary_conditions_input.LG_var.set(data['LG'])
        boundary_conditions_input.change_and_show_boundary()
        for _ in range(len(data['slG_list'])):
            boundary_conditions_input.slG_vars[_].set(data['slG_list'][_])

        for _ in range(len(data['YrlG_list'])):
            for __ in range(len(data['YrlG_list'][_])):
                boundary_conditions_input.yrlG_vars[_][__].set(
                    data['YrlG_list'][_][__])

         # desired conditions
        desired_conditions_input.I_var.set(data['I'])
        desired_conditions_input.change_and_show_desired()

        for _ in range(len(data['Li_list'])):
            desired_conditions_input.Li_vars[_].set(data['Li_list'][_])

        for _ in range(len(data['Ji_list'])):
            desired_conditions_input.Ji_vars[_].set(data['Ji_list'][_])
            desired_conditions_input.change_and_show_desired()

        for _ in range(len(data['sij_list'])):
            for __ in range(len(data['sij_list'][_])):
                desired_conditions_input.sij_vars[_][__].set(
                    data['sij_list'][_][__])

        desired_conditions_input.change_and_show_desired()
        for _ in range(len(data['Yij_list'])):
            for __ in range(len(data['Yij_list'][_])):
                desired_conditions_input.yij_vars[_][__].set(
                    data['Yij_list'][_][__])

    except Exception as e:
        raise e
