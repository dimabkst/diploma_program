from typing import Callable
from tkinter import *
from tkinter import ttk
from view.stock_problem import alpha_beta_gamma_window, stock_problem_window

ENTRY_WIDTH = 10


class stock_problem_page:

    def __init__(self, root, alpha_beta_gamma_solve_button_command: Callable, stock_problem_solve_button_command: Callable):
        try:
            s = ttk.Style()
            s.configure("TopWhiteBg.TFrame", background="white",
                        borderwidth=5, relief='raised')
            s.configure("WhiteBg.TFrame", background="white")

            # Frames
            self.root = ttk.Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.alpha_beta_gamma_button_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.alpha_beta_gamma_button_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.stock_problem_button_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.stock_problem_button_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            # Winbdows
            self.alpha_beta_gamma_solve_button_command = alpha_beta_gamma_solve_button_command
            self.alpha_beta_gamma_window = None

            self.stock_problem_solve_button_command = stock_problem_solve_button_command
            self.stock_problem_window = None

            # alpha_beta_gamma button
            self.alpha_beta_gamma_button = ttk.Button(self.alpha_beta_gamma_button_frame, text="Знайти альфа, бета, гамма",
                                                      command=self.alpha_beta_gamma_button_callback)
            self.alpha_beta_gamma_button.grid(
                column=0, row=0, sticky=(N, W, E, S))

            # stock_problem button
            self.stock_problem_button = ttk.Button(self.stock_problem_button_frame, text="Привести задачу керування динамікою щільності акцій",
                                                   command=self.stock_problem_button_callback)
            self.stock_problem_button.grid(
                column=0, row=0, sticky=(N, W, E, S))

            # Align
            self.align_rows_cols(self.alpha_beta_gamma_button_frame)
            self.align_rows_cols(self.stock_problem_button_frame)
            self.align_rows_cols(self.root)
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
            self.stock_problem_window = stock_problem_window(
                self.root, self.stock_problem_solve_button_command)
        except Exception as e:
            raise e

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
