from typing import Callable
from tkinter import N, E, W, S, Toplevel, StringVar
from tkinter.ttk import Label, Entry, Button
from view.utils import ENTRY_WIDTH, align_rows_cols, create_grid_frame, create_frame_label_entrie_frames


class alpha_beta_gamma_window:

    def __init__(self, root, solve_button_command: Callable):
        try:
            self.window = Toplevel(root)
            self.window.configure(bg="white")
            self.window.title("Альфа, бета, гамма")

            self.solve_button_command = solve_button_command

            # Frames
            self.input_rules_frame = create_grid_frame(
                root=self.window, column=0, row=0, style="TopWhiteBg.TFrame")

            self.input_frame = create_grid_frame(
                root=self.window, column=0, row=1, style="WhiteBg.TFrame")

            self.solve_button_frame = create_grid_frame(
                root=self.window, column=0, row=2, style="WhiteBg.TFrame")

            self.output_frame = create_grid_frame(
                root=self.window, column=0, row=3, style="WhiteBg.TFrame")

            # Input rules
            font = ("Arial", 14)
            Label(self.input_rules_frame,
                  text="mu, sigma - довільні додатні числа.\n\nb - довільне невід'ємне число.\n\nc - довільне число.",
                  font=font,
                  style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Input
            # mu input
            self.mu_frame, self.mu_label_frame, self.mu_entry_frame = create_frame_label_entrie_frames(
                root=self.input_frame, column=0, row=0, isRow=True, style="WhiteBg.TFrame")

            self.mu_var = StringVar()
            self.mu_var.set("0")

            Label(self.mu_label_frame, text="mu =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.mu_entry = Entry(
                self.mu_entry_frame, width=ENTRY_WIDTH, textvariable=self.mu_var)
            self.mu_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # sigma input
            self.sigma_frame, self.sigma_label_frame, self.sigma_entry_frame = create_frame_label_entrie_frames(
                root=self.input_frame, column=1, row=0, isRow=True, style="WhiteBg.TFrame")

            self.sigma_var = StringVar()
            self.sigma_var.set("0")

            Label(self.sigma_label_frame, text="sigma =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.sigma_entry = Entry(
                self.sigma_entry_frame, width=ENTRY_WIDTH, textvariable=self.sigma_var)
            self.sigma_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # b input
            self.b_frame, self.b_label_frame, self.b_entry_frame = create_frame_label_entrie_frames(
                root=self.input_frame, column=0, row=1, isRow=True, style="WhiteBg.TFrame")

            self.b_var = StringVar()
            self.b_var.set("0")

            Label(self.b_label_frame, text="b =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.b_entry = Entry(
                self.b_entry_frame, width=ENTRY_WIDTH, textvariable=self.b_var)
            self.b_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # c input
            self.c_frame, self.c_label_frame, self.c_entry_frame = create_frame_label_entrie_frames(
                root=self.input_frame, column=1, row=1, isRow=True, style="WhiteBg.TFrame")

            self.c_var = StringVar()
            self.c_var.set("0")

            Label(self.c_label_frame, text="c =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.c_entry = Entry(
                self.c_entry_frame, width=ENTRY_WIDTH, textvariable=self.c_var)
            self.c_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Solve button
            self.solve_button = Button(self.solve_button_frame, text="Знайти альфа, бета, гамма",
                                       command=self.solve_button_callback)
            self.solve_button.grid(column=0, row=0, sticky=(N, W, E, S))
            #

            # alpha output
            self.alpha_frame, self.alpha_label_frame, self.alpha_entry_frame = create_frame_label_entrie_frames(
                root=self.output_frame, column=0, row=0, isRow=True, style="WhiteBg.TFrame")

            self.alpha_var = StringVar()

            Label(self.alpha_label_frame, text="alpha =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.alpha_entry = Entry(
                self.alpha_entry_frame, width=ENTRY_WIDTH,
                textvariable=self.alpha_var, state='readonly')
            self.alpha_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # beta output
            self.beta_frame, self.beta_label_frame, self.beta_entry_frame = create_frame_label_entrie_frames(
                root=self.output_frame, column=0, row=1, isRow=True, style="WhiteBg.TFrame")

            self.beta_var = StringVar()

            Label(self.beta_label_frame, text="beta =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.beta_entry = Entry(
                self.beta_entry_frame, width=ENTRY_WIDTH,
                textvariable=self.beta_var, state='readonly')
            self.beta_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # gamma output
            self.gamma_frame, self.gamma_label_frame, self.gamma_entry_frame = create_frame_label_entrie_frames(
                root=self.output_frame, column=0, row=2, isRow=True, style="WhiteBg.TFrame")

            self.gamma_var = StringVar()

            Label(self.gamma_label_frame, text="gamma =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.gamma_entry = Entry(
                self.gamma_entry_frame, width=ENTRY_WIDTH,
                textvariable=self.gamma_var, state='readonly')
            self.gamma_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #
            #

            align_rows_cols(self.window)
        except Exception as e:
            raise e

    def solve_button_callback(self):
        try:
            self.solve_button_command()
        except Exception as e:
            raise e
