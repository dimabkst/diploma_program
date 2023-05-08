from typing import Callable
from tkinter import *
from tkinter import ttk
from view.utils import align_rows_cols

ENTRY_WIDTH = 10


class stock_problem_window:

    def __init__(self, root, solve_button_command: Callable):
        try:
            self.window = Toplevel(root)
            self.window.configure(bg="white")
            self.window.title(
                "Привести задачу керування динамікою щільності акцій")

            self.solve_button_command = solve_button_command

            # Frames
            self.input_rules_frame = ttk.Frame(
                self.window, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.input_rules_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.input_frame = ttk.Frame(
                self.window, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.input_frame.grid(
                column=0, row=1, sticky=(N, W, E, S))

            self.solve_button_frame = ttk.Frame(
                self.window, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.solve_button_frame.grid(
                column=0, row=2, sticky=(N, W, E, S))

            # Input rules
            font = ("Arial", 14)
            ttk.Label(self.input_rules_frame,
                      text="a, b - довільні додатні числа, b > a. T - довільне додатне число.\n\nI, J, K - довільні натуральні числа. xi, xk є [a, b]. tj, tk є [0, T].\n\nalpha, beta, gamma, uk - довільні числа.",
                      font=font,
                      style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Input
            # alpha input
            self.alpha_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.alpha_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.alpha_label_frame = ttk.Frame(
                self.alpha_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.alpha_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.alpha_entry_frame = ttk.Frame(
                self.alpha_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.alpha_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.alpha_var = StringVar()
            self.alpha_var.set("")

            ttk.Label(self.alpha_label_frame, text="alpha =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.alpha_entry = ttk.Entry(
                self.alpha_entry_frame, width=ENTRY_WIDTH, textvariable=self.alpha_var)
            self.alpha_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # beta input
            self.beta_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.beta_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            self.beta_label_frame = ttk.Frame(
                self.beta_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.beta_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.beta_entry_frame = ttk.Frame(
                self.beta_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.beta_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.beta_var = StringVar()
            self.beta_var.set("")

            ttk.Label(self.beta_label_frame, text="beta =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.beta_entry = ttk.Entry(
                self.beta_entry_frame, width=ENTRY_WIDTH, textvariable=self.beta_var)
            self.beta_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # gamma input
            self.gamma_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.gamma_frame.grid(
                column=2, row=0, sticky=(N, W, E, S))

            self.gamma_label_frame = ttk.Frame(
                self.gamma_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.gamma_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.gamma_entry_frame = ttk.Frame(
                self.gamma_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.gamma_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.gamma_var = StringVar()
            self.gamma_var.set("")

            ttk.Label(self.gamma_label_frame, text="gamma =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.gamma_entry = ttk.Entry(
                self.gamma_entry_frame, width=ENTRY_WIDTH, textvariable=self.gamma_var)
            self.gamma_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # a input
            self.a_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.a_frame.grid(
                column=0, row=1, sticky=(N, W, E, S))

            self.a_label_frame = ttk.Frame(
                self.a_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.a_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.a_entry_frame = ttk.Frame(
                self.a_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.a_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.a_var = StringVar()
            self.a_var.set("")

            ttk.Label(self.a_label_frame, text="a =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.a_entry = ttk.Entry(
                self.a_entry_frame, width=ENTRY_WIDTH, textvariable=self.a_var)
            self.a_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # b input
            self.b_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.b_frame.grid(
                column=1, row=1, sticky=(N, W, E, S))

            self.b_label_frame = ttk.Frame(
                self.b_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.b_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.b_entry_frame = ttk.Frame(
                self.b_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.b_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.b_var = StringVar()
            self.b_var.set("")

            ttk.Label(self.b_label_frame, text="b =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.b_entry = ttk.Entry(
                self.b_entry_frame, width=ENTRY_WIDTH, textvariable=self.b_var)
            self.b_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # T input
            self.T_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.T_frame.grid(
                column=2, row=1, sticky=(N, W, E, S))

            self.T_label_frame = ttk.Frame(
                self.T_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.T_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.T_entry_frame = ttk.Frame(
                self.T_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.T_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.T_var = StringVar()
            self.T_var.set("")

            ttk.Label(self.T_label_frame, text="T =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.T_entry = ttk.Entry(
                self.T_entry_frame, width=ENTRY_WIDTH, textvariable=self.T_var)
            self.T_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # I input
            self.I_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.I_frame.grid(
                column=0, row=2, sticky=(N, W, E, S))

            self.I_label_frame = ttk.Frame(
                self.I_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.I_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.I_entry_frame = ttk.Frame(
                self.I_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.I_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.I_var = StringVar()
            self.I_var.set("")
            self.I_var.trace("w", lambda name, index,
                             mode: self.change_and_show_stock_problem())

            ttk.Label(self.I_label_frame, text="I =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.I_entry = ttk.Entry(
                self.I_entry_frame, width=ENTRY_WIDTH, textvariable=self.I_var)
            self.I_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # xi_list input
            self.xi_list_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.xi_list_frame.grid(
                column=1, row=2, sticky=(N, W, E, S))

            self.xi_list_label_frame = ttk.Frame(
                self.xi_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.xi_list_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.xi_list_xi_frame = ttk.Frame(
                self.xi_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.xi_list_xi_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            self.xi_labels = []
            self.xi_vars = []
            self.xi_entries = []

            for i in range(int(self.I_var.get() or 0)):
                self.xi_vars.append(StringVar())
                self.xi_vars[i].set("")

                self.xi_labels.append(
                    ttk.Label(self.xi_list_xi_frame, text=f"x{i + 1}", style="WhiteBg.TLabel"))
                self.xi_labels[i].grid(row=0, column=i, sticky=(N, W, E, S))

                self.xi_entries.append(ttk.Entry(
                    self.xi_list_xi_frame, width=ENTRY_WIDTH, textvariable=self.xi_vars[i]))
                self.xi_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))

            ttk.Label(self.xi_list_label_frame, text="xi є [a, b]:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # J input
            self.J_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.J_frame.grid(
                column=0, row=3, sticky=(N, W, E, S))

            self.J_label_frame = ttk.Frame(
                self.J_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.J_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.J_entry_frame = ttk.Frame(
                self.J_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.J_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.J_var = StringVar()
            self.J_var.set("")
            self.J_var.trace("w", lambda name, index,
                             mode: self.change_and_show_stock_problem())

            ttk.Label(self.J_label_frame, text="J =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.J_entry = ttk.Entry(
                self.J_entry_frame, width=ENTRY_WIDTH, textvariable=self.J_var)
            self.J_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # tj_list input
            self.tj_list_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.tj_list_frame.grid(
                column=1, row=3, sticky=(N, W, E, S))

            self.tj_list_label_frame = ttk.Frame(
                self.tj_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.tj_list_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.tj_list_tj_frame = ttk.Frame(
                self.tj_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.tj_list_tj_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            self.tj_labels = []
            self.tj_vars = []
            self.tj_entries = []

            for j in range(int(self.J_var.get() or 0)):
                self.tj_vars.append(StringVar())
                self.tj_vars[j].set("")

                self.tj_labels.append(
                    ttk.Label(self.tj_list_tj_frame, text=f"t{j + 1}", style="WhiteBg.TLabel"))
                self.tj_labels[j].grid(row=0, column=j, sticky=(N, W, E, S))

                self.tj_entries.append(ttk.Entry(
                    self.tj_list_tj_frame, width=ENTRY_WIDTH, textvariable=self.tj_vars[j]))
                self.tj_entries[j].grid(row=1, column=j, sticky=(N, W, E, S))

            ttk.Label(self.tj_list_label_frame, text="tj є [0,T]:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # K input
            self.K_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.K_frame.grid(
                column=0, row=4, sticky=(N, W, E, S))

            self.K_label_frame = ttk.Frame(
                self.K_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.K_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.K_entry_frame = ttk.Frame(
                self.K_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.K_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.K_var = StringVar()
            self.K_var.set("")
            self.K_var.trace("w", lambda name, index,
                             mode: self.change_and_show_stock_problem())

            ttk.Label(self.K_label_frame, text="K =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.K_entry = ttk.Entry(
                self.K_entry_frame, width=ENTRY_WIDTH, textvariable=self.K_var)
            self.K_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # xk_list input
            self.xk_list_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.xk_list_frame.grid(
                column=1, row=4, sticky=(N, W, E, S))

            self.xk_list_label_frame = ttk.Frame(
                self.xk_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.xk_list_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.xk_list_xk_frame = ttk.Frame(
                self.xk_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.xk_list_xk_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            self.xk_labels = []
            self.xk_vars = []
            self.xk_entries = []

            for k in range(int(self.K_var.get() or 0)):
                self.xk_vars.append(StringVar())
                self.xk_vars[k].set("")

                self.xk_labels.append(
                    ttk.Label(self.xk_list_xk_frame, text=f"x{k + 1}", style="WhiteBg.TLabel"))
                self.xk_labels[k].grid(row=0, column=k, sticky=(N, W, E, S))

                self.xk_entries.append(ttk.Entry(
                    self.xk_list_xk_frame, width=ENTRY_WIDTH, textvariable=self.xk_vars[k]))
                self.xk_entries[k].grid(row=1, column=k, sticky=(N, W, E, S))

            ttk.Label(self.xk_list_label_frame, text="xk є [a,b]:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # tk_list input
            self.tk_list_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.tk_list_frame.grid(
                column=2, row=4, sticky=(N, W, E, S))

            self.tk_list_label_frame = ttk.Frame(
                self.tk_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.tk_list_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.tk_list_tk_frame = ttk.Frame(
                self.tk_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.tk_list_tk_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            self.tk_labels = []
            self.tk_vars = []
            self.tk_entries = []

            for k in range(int(self.K_var.get() or 0)):
                self.tk_vars.append(StringVar())
                self.tk_vars[k].set("")

                self.tk_labels.append(
                    ttk.Label(self.tk_list_tk_frame, text=f"t{k + 1}", style="WhiteBg.TLabel"))
                self.tk_labels[k].grid(row=0, column=k, sticky=(N, W, E, S))

                self.tk_entries.append(ttk.Entry(
                    self.tk_list_tk_frame, width=ENTRY_WIDTH, textvariable=self.tk_vars[k]))
                self.tk_entries[k].grid(row=1, column=k, sticky=(N, W, E, S))

            ttk.Label(self.tk_list_label_frame, text="tk є [0,T]:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # uk_list input
            self.uk_list_frame = ttk.Frame(
                self.input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.uk_list_frame.grid(
                column=3, row=4, sticky=(N, W, E, S))

            self.uk_list_label_frame = ttk.Frame(
                self.uk_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.uk_list_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.uk_list_uk_frame = ttk.Frame(
                self.uk_list_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.uk_list_uk_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            self.uk_labels = []
            self.uk_vars = []
            self.uk_entries = []

            for k in range(int(self.K_var.get() or 0)):
                self.uk_vars.append(StringVar())
                self.uk_vars[k].set("")

                self.uk_labels.append(
                    ttk.Label(self.uk_list_uk_frame, text=f"t{k + 1}", style="WhiteBg.TLabel"))
                self.uk_labels[k].grid(row=0, column=k, sticky=(N, W, E, S))

                self.uk_entries.append(ttk.Entry(
                    self.uk_list_uk_frame, width=ENTRY_WIDTH, textvariable=self.uk_vars[k]))
                self.uk_entries[k].grid(row=1, column=k, sticky=(N, W, E, S))

            ttk.Label(self.uk_list_label_frame, text="uk:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Solve button
            self.solve_button = ttk.Button(self.solve_button_frame, text="Привести задачу",
                                           command=self.solve_button_callback)
            self.solve_button.grid(column=0, row=0, sticky=(N, W, E, S))
            #

            # Align
            align_rows_cols(self.alpha_frame)
            align_rows_cols(self.alpha_label_frame)
            align_rows_cols(self.alpha_entry_frame)

            align_rows_cols(self.beta_frame)
            align_rows_cols(self.beta_label_frame)
            align_rows_cols(self.beta_entry_frame)

            align_rows_cols(self.gamma_frame)
            align_rows_cols(self.gamma_label_frame)
            align_rows_cols(self.gamma_entry_frame)

            align_rows_cols(self.a_frame)
            align_rows_cols(self.a_label_frame)
            align_rows_cols(self.a_entry_frame)

            align_rows_cols(self.b_frame)
            align_rows_cols(self.b_label_frame)
            align_rows_cols(self.b_entry_frame)

            align_rows_cols(self.T_frame)
            align_rows_cols(self.T_label_frame)
            align_rows_cols(self.T_entry_frame)

            align_rows_cols(self.I_frame)
            align_rows_cols(self.I_label_frame)
            align_rows_cols(self.I_entry_frame)

            align_rows_cols(self.xi_list_frame)
            align_rows_cols(self.xi_list_label_frame)
            align_rows_cols(self.xi_list_xi_frame)

            align_rows_cols(self.J_frame)
            align_rows_cols(self.J_label_frame)
            align_rows_cols(self.J_entry_frame)

            align_rows_cols(self.tj_list_frame)
            align_rows_cols(self.tj_list_label_frame)
            align_rows_cols(self.tj_list_tj_frame)

            align_rows_cols(self.K_frame)
            align_rows_cols(self.K_label_frame)
            align_rows_cols(self.K_entry_frame)

            align_rows_cols(self.xk_list_frame)
            align_rows_cols(self.xk_list_label_frame)
            align_rows_cols(self.xk_list_xk_frame)

            align_rows_cols(self.tk_list_frame)
            align_rows_cols(self.tk_list_label_frame)
            align_rows_cols(self.tk_list_tk_frame)

            align_rows_cols(self.uk_list_frame)
            align_rows_cols(self.uk_list_label_frame)
            align_rows_cols(self.uk_list_uk_frame)

            align_rows_cols(self.input_frame)

            align_rows_cols(self.solve_button_frame)

            align_rows_cols(self.window)
            #

            self.window.protocol("WM_DELETE_WINDOW",
                                 self.close_window_callback)
            self.window.withdraw()
        except Exception as e:
            raise e

    def solve_button_callback(self):
        try:
            self.solve_button_command()
        except Exception as e:
            raise e

    def change_and_show_xi(self):
        try:
            if self.I_var.get() and int(self.I_var.get()) > 0:
                old_count = len(self.xi_vars)
                for i in range(max(old_count, int(self.I_var.get() or 0))):
                    if i >= min(old_count, int(self.I_var.get() or 0)):
                        if old_count > int(self.I_var.get() or 0):
                            self.xi_vars = self.xi_vars[0:i]

                            for ii in range(i, old_count):
                                self.xi_labels[ii].destroy()
                                self.xi_entries[ii].destroy()

                            self.xi_labels = self.xi_labels[0:i]
                            self.xi_entries = self.xi_entries[0:i]
                            break
                        else:
                            self.xi_vars.append(StringVar())

                            self.xi_labels.append(
                                ttk.Label(self.xi_list_xi_frame, text=f"x{i + 1}", style="WhiteBg.TLabel"))
                            self.xi_entries.append(
                                ttk.Entry(self.xi_list_xi_frame, width=ENTRY_WIDTH,
                                          textvariable=self.xi_vars[i]))

                            self.xi_vars[i].set("")
                            self.xi_labels[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))
                            self.xi_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_tj(self):
        try:
            if self.J_var.get() and int(self.J_var.get()) > 0:
                old_count = len(self.tj_vars)
                for i in range(max(old_count, int(self.J_var.get() or 0))):
                    if i >= min(old_count, int(self.J_var.get() or 0)):
                        if old_count > int(self.J_var.get() or 0):
                            self.tj_vars = self.tj_vars[0:i]

                            for ii in range(i, old_count):
                                self.tj_labels[ii].destroy()
                                self.tj_entries[ii].destroy()

                            self.tj_labels = self.tj_labels[0:i]
                            self.tj_entries = self.tj_entries[0:i]
                            break
                        else:
                            self.tj_vars.append(StringVar())

                            self.tj_labels.append(
                                ttk.Label(self.tj_list_tj_frame, text=f"t{i + 1}", style="WhiteBg.TLabel"))
                            self.tj_entries.append(
                                ttk.Entry(self.tj_list_tj_frame, width=ENTRY_WIDTH,
                                          textvariable=self.tj_vars[i]))

                            self.tj_vars[i].set("")
                            self.tj_labels[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))
                            self.tj_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_xk(self):
        try:
            if self.K_var.get() and int(self.K_var.get()) > 0:
                old_count = len(self.xk_vars)
                for i in range(max(old_count, int(self.K_var.get() or 0))):
                    if i >= min(old_count, int(self.K_var.get() or 0)):
                        if old_count > int(self.K_var.get() or 0):
                            self.xk_vars = self.xk_vars[0:i]

                            for ii in range(i, old_count):
                                self.xk_labels[ii].destroy()
                                self.xk_entries[ii].destroy()

                            self.xk_labels = self.xk_labels[0:i]
                            self.xk_entries = self.xk_entries[0:i]
                            break
                        else:
                            self.xk_vars.append(StringVar())

                            self.xk_labels.append(
                                ttk.Label(self.xk_list_xk_frame, text=f"x{i + 1}", style="WhiteBg.TLabel"))
                            self.xk_entries.append(
                                ttk.Entry(self.xk_list_xk_frame, width=ENTRY_WIDTH,
                                          textvariable=self.xk_vars[i]))

                            self.xk_vars[i].set("")
                            self.xk_labels[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))
                            self.xk_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_tk(self):
        try:
            if self.K_var.get() and int(self.K_var.get()) > 0:
                old_count = len(self.tk_vars)
                for i in range(max(old_count, int(self.K_var.get() or 0))):
                    if i >= min(old_count, int(self.K_var.get() or 0)):
                        if old_count > int(self.K_var.get() or 0):
                            self.tk_vars = self.tk_vars[0:i]

                            for ii in range(i, old_count):
                                self.tk_labels[ii].destroy()
                                self.tk_entries[ii].destroy()

                            self.tk_labels = self.tk_labels[0:i]
                            self.tk_entries = self.tk_entries[0:i]
                            break
                        else:
                            self.tk_vars.append(StringVar())

                            self.tk_labels.append(
                                ttk.Label(self.tk_list_tk_frame, text=f"t{i + 1}", style="WhiteBg.TLabel"))
                            self.tk_entries.append(
                                ttk.Entry(self.tk_list_tk_frame, width=ENTRY_WIDTH,
                                          textvariable=self.tk_vars[i]))

                            self.tk_vars[i].set("")
                            self.tk_labels[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))
                            self.tk_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_uk(self):
        try:
            if self.K_var.get() and int(self.K_var.get()) > 0:
                old_count = len(self.uk_vars)
                for i in range(max(old_count, int(self.K_var.get() or 0))):
                    if i >= min(old_count, int(self.K_var.get() or 0)):
                        if old_count > int(self.K_var.get() or 0):
                            self.uk_vars = self.uk_vars[0:i]

                            for ii in range(i, old_count):
                                self.uk_labels[ii].destroy()
                                self.uk_entries[ii].destroy()

                            self.uk_labels = self.uk_labels[0:i]
                            self.uk_entries = self.uk_entries[0:i]
                            break
                        else:
                            self.uk_vars.append(StringVar())

                            self.uk_labels.append(
                                ttk.Label(self.uk_list_uk_frame, text=f"u{i + 1}", style="WhiteBg.TLabel"))
                            self.uk_entries.append(
                                ttk.Entry(self.uk_list_uk_frame, width=ENTRY_WIDTH,
                                          textvariable=self.uk_vars[i]))

                            self.uk_vars[i].set("")
                            self.uk_labels[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))
                            self.uk_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_stock_problem(self):
        try:
            self.change_and_show_xi()
            self.change_and_show_tj()
            self.change_and_show_xk()
            self.change_and_show_tk()
            self.change_and_show_uk()
        except Exception as e:
            raise e

    def close_window_callback(self):
        self.window.withdraw()
