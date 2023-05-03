import logging
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view import problem_conditions_input, initial_boundary_desired_conditions_input, solve_button, v_input, save_load, results_output, input_rules, settings_input, console_output
from controller import control, view_data_to_file, file_data_to_view


class View:

    def __init__(self, file_path):
        """

    :param file_path: string with path to the file with data
        """
        try:
            self.root = Tk()
            self.root.configure(bg="white")
            self.root.title("Керування просторово-часовим процесом")

            self.notebook = ttk.Notebook(self.root)
            self.notebook.grid(column=0, row=0, sticky=(N, E, W, S))

            self.save_load = save_load(self.root, file_path,
                                       lambda _file_path: view_data_to_file(
                                           self, _file_path),
                                       lambda _file_path: file_data_to_view(self, _file_path))
            self.input_rules = input_rules(self.root)
            self.problem_conditions_input = problem_conditions_input(self.root)
            self.initial_boundary_desired_conditions_input = initial_boundary_desired_conditions_input(
                self.root)
            self.v_input = v_input(self.root)
            self.settings_input = settings_input(self.root)
            self.solve_button = solve_button(
                self.root, lambda: self.solve_button_command(file_path))
            self.results_output = results_output(self.root)
            self.console_output = console_output(self.root)

            self.notebook.add(self.save_load.root, text='Зберегти/Завантажити')
            self.notebook.add(self.input_rules.root, text='Правила вводу')
            self.notebook.add(
                self.problem_conditions_input.root, text='Умови задачі')
            self.notebook.add(
                self.initial_boundary_desired_conditions_input.root, text='Початкові, крайові та бажані умови')
            self.notebook.add(self.v_input.root, text='Ввід v(x,t)')
            self.notebook.add(self.settings_input.root, text='Налаштування')
            self.notebook.add(self.solve_button.root, text="Розв'язати задачу")
            self.notebook.add(self.results_output.root, text="Результати")
            self.notebook.add(self.console_output.root, text="Вивід консолі")

            self.notebook.bind("<<NotebookTabChanged>>",
                               func=self.notebook_tab_changed_callback)

            self.align_rows_cols(self.notebook)
            self.align_rows_cols(self.root)

            self.root.mainloop()
        except Exception as e:
            raise e

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)

    def solve_button_command(self, file_path: str):
        try:
            control(self, file_path)
        except Exception as e:
            messagebox.showerror('Помилка', str(e))
            logging.error(e, exc_info=True)

    def update_dynamic_data(self):
        try:
            pci = self.problem_conditions_input
            S = pci.S_var.get()
            S0 = pci.S0_var.get()
            SG = pci.SG_var.get()
            T = pci.T_var.get()

            self.initial_boundary_desired_conditions_input.change_S0_SG_T(
                S0, SG, T)
            self.settings_input.change_S_S0_SG_T(S, S0, SG, T)
        except Exception as e:
            raise e

    def notebook_tab_changed_callback(self, event):
        try:
            self.update_dynamic_data()
        except Exception as e:
            raise e
