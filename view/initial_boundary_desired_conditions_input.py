from tkinter import N, E, W, S, StringVar, HORIZONTAL
from tkinter.ttk import Frame, Label, Entry, Scrollbar
from .initial_conditions_input import initial_conditions_input
from .boundary_conditions_input import boundary_conditions_input
from .desired_conditions_input import desired_conditions_input
from view.utils import ENTRY_WIDTH, align_rows_cols


class initial_boundary_desired_conditions_input:

    def __init__(self, root):
        try:
            # Frames
            self.root = Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.initial_frame = Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.initial_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            self.boundary_frame = Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.boundary_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.desired_frame = Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.desired_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.S0_SG_T_frame = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.S0_SG_T_frame.grid(column=1, row=1, sticky=(N, W, E, S))

            # Conditions input
            self.initial_conditions_input = initial_conditions_input(
                self.initial_frame)
            self.boundary_conditions_input = boundary_conditions_input(
                self.boundary_frame)
            self.desired_conditions_input = desired_conditions_input(
                self.desired_frame)

            # S0,SG,T info
            # S0
            self.S0_frame = Frame(
                self.S0_SG_T_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.S0_frame.grid(column=0, row=0, sticky=(N, W, E, S))

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
                self.S0_SG_T_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
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
                self.S0_SG_T_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.T_frame.grid(column=0, row=2, sticky=(N, W, E, S))

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

            # Align
            align_rows_cols(self.initial_frame)

            align_rows_cols(self.boundary_frame)

            align_rows_cols(self.desired_frame)

            align_rows_cols(self.S0_entry_frame)
            align_rows_cols(self.S0_label_frame)
            align_rows_cols(self.S0_frame)
            align_rows_cols(self.SG_entry_frame)
            align_rows_cols(self.SG_label_frame)
            align_rows_cols(self.SG_frame)
            align_rows_cols(self.T_entry_frame)
            align_rows_cols(self.T_label_frame)
            align_rows_cols(self.T_frame)
            align_rows_cols(self.S0_SG_T_frame)

            align_rows_cols(self.root)
        except Exception as e:
            raise e

    def change_S0_SG_T(self, S0: str, SG: str, T: str):
        try:
            self.S0_var.set(S0)
            self.SG_var.set(SG)
            self.T_var.set(T)
        except Exception as e:
            raise e
