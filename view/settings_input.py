from tkinter import N, E, W, S, StringVar, HORIZONTAL
from tkinter.ttk import Style, Frame, Label, Entry, Scrollbar
from view.utils import align_rows_cols

ENTRY_WIDTH = 10


class settings_input:

    def __init__(self, root):
        try:
            s = Style()
            s.configure("TopWhiteBg.TFrame", background="white",
                        borderwidth=5, relief='raised')
            s.configure("WhiteBg.TFrame", background="white")
            s.configure("WhiteBg.TLabel", background="white")

            # Frames
            self.root = Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.integrals_precision_frame = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.integrals_precision_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.plot_grid_dimension_frame = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.plot_grid_dimension_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            self.plot_limits_frame = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.plot_limits_frame.grid(
                column=0, row=1, sticky=(N, W, E, S))

            self.S_S0_SG_T_frame = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.S_S0_SG_T_frame.grid(column=1, row=1, sticky=(N, W, E, S))

            # integrals_precision_input
            self.integrals_precision_label_frame = Frame(
                self.integrals_precision_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.integrals_precision_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.integrals_precision_entry_frame = Frame(
                self.integrals_precision_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.integrals_precision_entry_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            Label(self.integrals_precision_label_frame, text="Точність обчислення інтегралів - ", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.integrals_precision_var = StringVar()
            self.integrals_precision_var.set("1.5e-3")

            self.integrals_precision_entry = Entry(
                self.integrals_precision_entry_frame, width=ENTRY_WIDTH, textvariable=self.integrals_precision_var)
            self.integrals_precision_entry.grid(
                column=0, row=0, sticky=(N, E, W, S))
            #

            # plot_grid_dimension_input
            self.plot_grid_dimension_label_frame = Frame(
                self.plot_grid_dimension_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.plot_grid_dimension_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.plot_grid_dimension_entry_frame = Frame(
                self.plot_grid_dimension_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.plot_grid_dimension_entry_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            Label(self.plot_grid_dimension_label_frame, text="Розмірність сітки графіка - ", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.plot_grid_dimension_var = StringVar()
            self.plot_grid_dimension_var.set("20")

            self.plot_grid_dimension_entry = Entry(
                self.plot_grid_dimension_entry_frame, width=ENTRY_WIDTH, textvariable=self.plot_grid_dimension_var)
            self.plot_grid_dimension_entry.grid(
                column=0, row=0, sticky=(N, E, W, S))
            #

            # plot_limits_input
            # X0
            self.X0_label_frame = Frame(
                self.plot_limits_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.X0_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.X0_entry_frame = Frame(
                self.plot_limits_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.X0_entry_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            Label(self.X0_label_frame, text="Крайня ліва межа осі X - X0  =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.X0_var = StringVar()
            self.X0_var.set("0")

            self.X0_entry = Entry(
                self.X0_entry_frame, width=ENTRY_WIDTH, textvariable=self.X0_var)
            self.X0_entry.grid(
                column=0, row=0, sticky=(N, E, W, S))

            # X1
            self.X1_label_frame = Frame(
                self.plot_limits_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.X1_label_frame.grid(
                column=2, row=0, sticky=(N, W, E, S))

            self.X1_entry_frame = Frame(
                self.plot_limits_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.X1_entry_frame.grid(
                column=3, row=0, sticky=(N, W, E, S))

            Label(self.X1_label_frame, text="Крайня права межа осі X - X1 =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.X1_var = StringVar()
            self.X1_var.set("1")

            self.X1_entry = Entry(
                self.X1_entry_frame, width=ENTRY_WIDTH, textvariable=self.X1_var)
            self.X1_entry.grid(
                column=0, row=0, sticky=(N, E, W, S))
            #

            # T0
            self.T0_label_frame = Frame(
                self.plot_limits_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.T0_label_frame.grid(
                column=0, row=1, sticky=(N, W, E, S))

            self.T0_entry_frame = Frame(
                self.plot_limits_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.T0_entry_frame.grid(
                column=1, row=1, sticky=(N, W, E, S))

            Label(self.T0_label_frame, text="Крайня ліва межа осі T - T0 =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.T0_var = StringVar()
            self.T0_var.set("0")

            self.T0_entry = Entry(
                self.T0_entry_frame, width=ENTRY_WIDTH, textvariable=self.T0_var)
            self.T0_entry.grid(
                column=0, row=0, sticky=(N, E, W, S))
            #

            # T1
            self.T1_label_frame = Frame(
                self.plot_limits_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.T1_label_frame.grid(
                column=2, row=1, sticky=(N, W, E, S))

            self.T1_entry_frame = Frame(
                self.plot_limits_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.T1_entry_frame.grid(
                column=3, row=1, sticky=(N, W, E, S))

            Label(self.T1_label_frame, text="Крайня права межа осі T - T1 =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.T1_var = StringVar()
            self.T1_var.set("1")

            self.T1_entry = Entry(
                self.T1_entry_frame, width=ENTRY_WIDTH, textvariable=self.T1_var)
            self.T1_entry.grid(
                column=0, row=0, sticky=(N, E, W, S))
            #

            # S,S0,SG,T info
            # S
            self.S_frame = Frame(
                self.S_S0_SG_T_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.S_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            self.S_label_frame = Frame(
                self.S_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.S_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.S_entry_frame = Frame(
                self.S_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.S_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.S_var = StringVar()
            self.S_var.set("[0, 1]")

            Label(self.S_label_frame, text="S =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.S_entry = Entry(
                self.S_entry_frame, width=ENTRY_WIDTH, textvariable=self.S_var, state="readonly")
            self.S_entry_hsb = Scrollbar(
                self.S_entry_frame, orient=HORIZONTAL, command=self.S_entry.xview)
            self.S_entry.configure(xscrollcommand=self.S_entry_hsb.set)
            self.S_entry_hsb.grid(column=0, row=1, sticky=(E, W))
            self.S_entry.grid(column=0, row=0, sticky=(N, E, W, S))

            # S0
            self.S0_frame = Frame(
                self.S_S0_SG_T_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.S0_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.S0_label_frame = Frame(
                self.S0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.S0_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.S0_entry_frame = Frame(
                self.S0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.S0_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.S0_var = StringVar()
            self.S0_var.set("[0, 1]")

            Label(self.S0_label_frame, text="S0 =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.S0_entry = Entry(
                self.S0_entry_frame, width=ENTRY_WIDTH, textvariable=self.S0_var, state="readonly")
            self.S0_entry_hsb = Scrollbar(
                self.S0_entry_frame, orient=HORIZONTAL, command=self.S0_entry.xview)
            self.S0_entry.configure(xscrollcommand=self.S0_entry_hsb.set)
            self.S0_entry_hsb.grid(column=0, row=1, sticky=(E, W))
            self.S0_entry.grid(column=0, row=0, sticky=(N, E, W, S))

            # SG
            self.SG_frame = Frame(
                self.S_S0_SG_T_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.SG_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.SG_label_frame = Frame(
                self.SG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.SG_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.SG_entry_frame = Frame(
                self.SG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.SG_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.SG_var = StringVar()
            self.SG_var.set("[0, 1]")

            Label(self.SG_label_frame, text="SG =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.SG_entry = Entry(
                self.SG_entry_frame, width=ENTRY_WIDTH, textvariable=self.SG_var, state="readonly")
            self.SG_entry_hsb = Scrollbar(
                self.SG_entry_frame, orient=HORIZONTAL, command=self.SG_entry.xview)
            self.SG_entry.configure(xscrollcommand=self.SG_entry_hsb.set)
            self.SG_entry_hsb.grid(column=0, row=1, sticky=(E, W))
            self.SG_entry.grid(column=0, row=0, sticky=(N, E, W, S))

            # T
            self.T_frame = Frame(
                self.S_S0_SG_T_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.T_frame.grid(column=1, row=1, sticky=(N, W, E, S))

            self.T_label_frame = Frame(
                self.T_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.T_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.T_entry_frame = Frame(
                self.T_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.T_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.T_var = StringVar()
            self.T_var.set("1")

            Label(self.T_label_frame, text="T =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.T_entry = Entry(
                self.T_entry_frame, width=ENTRY_WIDTH, textvariable=self.T_var, state="readonly")
            self.T_entry.grid(column=0, row=0, sticky=(N, E, W, S))

            # Align everything
            align_rows_cols(self.integrals_precision_frame)
            align_rows_cols(self.integrals_precision_label_frame)
            align_rows_cols(self.integrals_precision_entry_frame)

            align_rows_cols(self.plot_grid_dimension_frame)
            align_rows_cols(self.plot_grid_dimension_label_frame)
            align_rows_cols(self.plot_grid_dimension_entry_frame)

            align_rows_cols(self.plot_limits_frame)
            align_rows_cols(self.X0_label_frame)
            align_rows_cols(self.X0_entry_frame)
            align_rows_cols(self.X1_label_frame)
            align_rows_cols(self.X1_entry_frame)
            align_rows_cols(self.T0_label_frame)
            align_rows_cols(self.T0_entry_frame)
            align_rows_cols(self.T1_label_frame)
            align_rows_cols(self.T1_entry_frame)

            align_rows_cols(self.S_entry_frame)
            align_rows_cols(self.S_label_frame)
            align_rows_cols(self.S_frame)
            align_rows_cols(self.S0_entry_frame)
            align_rows_cols(self.S0_label_frame)
            align_rows_cols(self.S0_frame)
            align_rows_cols(self.SG_entry_frame)
            align_rows_cols(self.SG_label_frame)
            align_rows_cols(self.SG_frame)
            align_rows_cols(self.T_entry_frame)
            align_rows_cols(self.T_label_frame)
            align_rows_cols(self.T_frame)
            align_rows_cols(self.S_S0_SG_T_frame)

            align_rows_cols(self.root)
        except Exception as e:
            raise e

    def change_S_S0_SG_T(self, S: str, S0: str, SG: str, T: str):
        try:
            self.S_var.set(S)
            self.S0_var.set(S0)
            self.SG_var.set(SG)
            self.T_var.set(T)
        except Exception as e:
            raise e
