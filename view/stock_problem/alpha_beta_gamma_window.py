from typing import Callable
from tkinter import N, E, W, S, Toplevel, StringVar
from tkinter.ttk import Frame, Label, Entry, Button
from view.utils import align_rows_cols

ENTRY_WIDTH = 10


class alpha_beta_gamma_window:

    def __init__(self, root, solve_button_command: Callable):
        try:
            self.window = Toplevel(root)
            self.window.configure(bg="white")
            self.window.title("Альфа, бета, гамма")

            self.solve_button_command = solve_button_command

            # Frames
            self.input_rules_frame = Frame(
                self.window, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.input_rules_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.input_frame = Frame(
                self.window, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.input_frame.grid(
                column=0, row=1, sticky=(N, W, E, S))

            self.solve_button_frame = Frame(
                self.window, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.solve_button_frame.grid(
                column=0, row=2, sticky=(N, W, E, S))

            self.output_frame = Frame(
                self.window, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.output_frame.grid(
                column=0, row=3, sticky=(N, W, E, S))

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
            self.mu_frame = Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.mu_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.mu_label_frame = Frame(
                self.mu_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.mu_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.mu_entry_frame = Frame(
                self.mu_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.mu_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.mu_var = StringVar()
            self.mu_var.set("0")

            Label(self.mu_label_frame, text="mu =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.mu_entry = Entry(
                self.mu_entry_frame, width=ENTRY_WIDTH, textvariable=self.mu_var)
            self.mu_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # sigma input
            self.sigma_frame = Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.sigma_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            self.sigma_label_frame = Frame(
                self.sigma_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.sigma_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.sigma_entry_frame = Frame(
                self.sigma_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.sigma_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.sigma_var = StringVar()
            self.sigma_var.set("0")

            Label(self.sigma_label_frame, text="sigma =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.sigma_entry = Entry(
                self.sigma_entry_frame, width=ENTRY_WIDTH, textvariable=self.sigma_var)
            self.sigma_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # b input
            self.b_frame = Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.b_frame.grid(
                column=0, row=1, sticky=(N, W, E, S))

            self.b_label_frame = Frame(
                self.b_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.b_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.b_entry_frame = Frame(
                self.b_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.b_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.b_var = StringVar()
            self.b_var.set("0")

            Label(self.b_label_frame, text="b =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.b_entry = Entry(
                self.b_entry_frame, width=ENTRY_WIDTH, textvariable=self.b_var)
            self.b_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # c input
            self.c_frame = Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.c_frame.grid(
                column=1, row=1, sticky=(N, W, E, S))

            self.c_label_frame = Frame(
                self.c_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.c_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.c_entry_frame = Frame(
                self.c_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.c_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

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
            self.alpha_frame = Frame(
                self.output_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.alpha_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.alpha_label_frame = Frame(
                self.alpha_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.alpha_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.alpha_entry_frame = Frame(
                self.alpha_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.alpha_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.alpha_var = StringVar()

            Label(self.alpha_label_frame, text="alpha =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.alpha_entry = Entry(
                self.alpha_entry_frame, width=ENTRY_WIDTH,
                textvariable=self.alpha_var, state='readonly')
            self.alpha_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # beta output
            self.beta_frame = Frame(
                self.output_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.beta_frame.grid(
                column=0, row=1, sticky=(N, W, E, S))

            self.beta_label_frame = Frame(
                self.beta_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.beta_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.beta_entry_frame = Frame(
                self.beta_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.beta_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.beta_var = StringVar()

            Label(self.beta_label_frame, text="beta =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.beta_entry = Entry(
                self.beta_entry_frame, width=ENTRY_WIDTH,
                textvariable=self.beta_var, state='readonly')
            self.beta_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # gamma output
            self.gamma_frame = Frame(
                self.output_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.gamma_frame.grid(
                column=0, row=2, sticky=(N, W, E, S))

            self.gamma_label_frame = Frame(
                self.gamma_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.gamma_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.gamma_entry_frame = Frame(
                self.gamma_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.gamma_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.gamma_var = StringVar()

            Label(self.gamma_label_frame, text="gamma =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.gamma_entry = Entry(
                self.gamma_entry_frame, width=ENTRY_WIDTH,
                textvariable=self.gamma_var, state='readonly')
            self.gamma_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #
            #

            # Align
            align_rows_cols(self.mu_frame)
            align_rows_cols(self.mu_label_frame)
            align_rows_cols(self.mu_entry_frame)

            align_rows_cols(self.sigma_frame)
            align_rows_cols(self.sigma_label_frame)
            align_rows_cols(self.sigma_entry_frame)

            align_rows_cols(self.b_frame)
            align_rows_cols(self.b_label_frame)
            align_rows_cols(self.b_entry_frame)

            align_rows_cols(self.c_frame)
            align_rows_cols(self.c_label_frame)
            align_rows_cols(self.c_entry_frame)

            align_rows_cols(self.input_frame)

            align_rows_cols(self.solve_button_frame)

            align_rows_cols(self.alpha_frame)
            align_rows_cols(self.alpha_label_frame)
            align_rows_cols(self.alpha_entry_frame)

            align_rows_cols(self.beta_frame)
            align_rows_cols(self.beta_label_frame)
            align_rows_cols(self.beta_entry_frame)

            align_rows_cols(self.gamma_frame)
            align_rows_cols(self.gamma_label_frame)
            align_rows_cols(self.gamma_entry_frame)

            align_rows_cols(self.output_frame)

            align_rows_cols(self.window)
            #
        except Exception as e:
            raise e

    def solve_button_callback(self):
        try:
            self.solve_button_command()
        except Exception as e:
            raise e
