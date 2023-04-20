from tkinter import *
from tkinter import ttk
from .problem_conditions_input import problem_conditions_input
from .boundary_desired_conditions_input import boundary_desired_conditions_input
from .solve_button import solve_button
from .v_input import v_input
from .save_load import save_load
from .results_output import results_output
from controller import control, view_data_to_file, file_data_to_view


class View:

    def __init__(self, file_path):
        """

    :param file_path: string with path to the file with data
        """
        try:
            self.root = Tk()
            self.root.configure(bg="white")
            self.root.title("Математичне моделювання. Лабораторна робота №3")

            self.notebook = ttk.Notebook(self.root)
            self.notebook.grid(column=0, row=0, sticky=(N, E, W, S))

            self.save_load = save_load(self.root, file_path,
                                       lambda _file_path: view_data_to_file(self, _file_path),
                                       lambda _file_path: file_data_to_view(self, _file_path))
            self.problem_conditions_input = problem_conditions_input(self.root)
            self.boundary_desired_conditions_input = boundary_desired_conditions_input(self.root)
            self.v_input = v_input(self.root)
            self.solve_button = solve_button(self.root, lambda: self.solve_button_command(file_path))
            self.results_output = results_output(self.root)

            self.notebook.add(self.save_load.root, text='Зберегти/Завантажити')
            self.notebook.add(self.problem_conditions_input.root, text='Умови задачі')
            self.notebook.add(self.boundary_desired_conditions_input.root, text='Крайові та бажані умови')
            self.notebook.add(self.v_input.root, text='Ввід v(x,t)')
            self.notebook.add(self.solve_button.root, text="Розв'язати задачу")
            self.notebook.add(self.results_output.root, text="Результати")

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
            raise e
