from typing import Callable
from tkinter import N, E, W, S
from tkinter.ttk import Button
from view.stock_problem import alpha_beta_gamma_window, stock_problem_window
from view.utils import align_rows_cols, create_grid_frame


class stock_problem_page:

    def __init__(self, root, alpha_beta_gamma_solve_button_command: Callable, stock_problem_solve_button_command: Callable):
        try:
            # Frames
            self.root = create_grid_frame(
                root=root, column=0, row=0, style="TopWhiteBg.TFrame")

            self.alpha_beta_gamma_button_frame = create_grid_frame(
                root=self.root, column=0, row=0, style="WhiteBg.TFrame")

            self.stock_problem_button_frame = create_grid_frame(
                root=self.root, column=1, row=0, style="WhiteBg.TFrame")

            # Winbdows
            self.alpha_beta_gamma_solve_button_command = alpha_beta_gamma_solve_button_command
            self.alpha_beta_gamma_window = None

            self.stock_problem_solve_button_command = stock_problem_solve_button_command
            self.stock_problem_window = stock_problem_window(
                self.root, self.stock_problem_solve_button_command)

            # alpha_beta_gamma button
            self.alpha_beta_gamma_button = Button(self.alpha_beta_gamma_button_frame, text="Знайти альфа, бета, гамма",
                                                  command=self.alpha_beta_gamma_button_callback)
            self.alpha_beta_gamma_button.grid(
                column=0, row=0, sticky=(N, W, E, S))

            # stock_problem button
            self.stock_problem_button = Button(self.stock_problem_button_frame, text="Привести задачу керування динамікою щільності акцій",
                                               command=self.stock_problem_button_callback)
            self.stock_problem_button.grid(
                column=0, row=0, sticky=(N, W, E, S))

            align_rows_cols(self.root)
        except Exception as e:
            raise e

    def alpha_beta_gamma_button_callback(self):
        try:
            self.alpha_beta_gamma_window = alpha_beta_gamma_window(
                self.root, self.alpha_beta_gamma_solve_button_command)
        except Exception as e:
            raise e

    def stock_problem_button_callback(self):
        try:
            self.stock_problem_window.window.deiconify()
        except Exception as e:
            raise e
