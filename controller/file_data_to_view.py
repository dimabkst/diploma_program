from controller import retrieve_data_from_file
from tkinter import StringVar
import numpy as np


def file_data_to_view(view, file_path: str) -> None:
    """

    :param view: object of View class in which to save
    :param file_path: string with path to the file from which to load
    :return: None
    """
    try:
        problem_conditions_input = view.problem_conditions_input
        initial_conditions_input = view.initial_boundary_desired_conditions_input.initial_conditions_input
        boundary_conditions_input = view.initial_boundary_desired_conditions_input.boundary_conditions_input
        desired_conditions_input = view.initial_boundary_desired_conditions_input.desired_conditions_input
        v_input = view.v_input
        settings_input = view.settings_input
        results_output = view.results_output

        # reading json file
        data = retrieve_data_from_file(file_path)

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

        # v
        v_input.count_var.set(len(data['v0_list']))
        v_input.change_and_show_v()

        for _ in range(len(data['v0_list'])):
            v_input.v0_vars[-1].set(data['v0_list'][_])

        for _ in range(len(data['vG_list'])):
            v_input.vG_vars[-1].set(data['vG_list'][_])

        # settings
        settings_input.integrals_precision_var.set(data['integrals_precision'])
        settings_input.plot_grid_dimension_var.set(data['plot_grid_dimension'])

        settings_input.X0_var.set(data['X0'])
        settings_input.X1_var.set(data['X1'])
        settings_input.T0_var.set(data['T0'])
        settings_input.T1_var.set(data['T1'])

        # solutions
        if data.get('solutions'):
            solutions = data.get('solutions')
            for sol in solutions:
                sol['solution_plot_data'] = {
                    key: np.array(item) for key, item in sol['solution_plot_data'].items()}
                sol['Yrl0'] = np.array(sol['Yrl0'])

            results_output.receive_data_and_show_it(solutions)

    except Exception as e:
        raise e
