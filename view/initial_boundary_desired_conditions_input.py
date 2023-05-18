from tkinter import N, E, W, S, StringVar, HORIZONTAL
from tkinter.ttk import Label, Entry, Scrollbar
from .initial_conditions_input import initial_conditions_input
from .boundary_conditions_input import boundary_conditions_input
from .desired_conditions_input import desired_conditions_input
from view.utils import ENTRY_WIDTH, create_grid_frame


class initial_boundary_desired_conditions_input:

    def __init__(self, root):
        try:
            # Frames
            self.root = create_grid_frame(
                root=root, column=0, row=0, style="TopWhiteBg.TFrame")

            self.initial_frame = create_grid_frame(
                root=self.root, column=0, row=0, style="WhiteBg.TFrame")

            self.boundary_frame = create_grid_frame(
                root=self.root, column=0, row=1, style="WhiteBg.TFrame")

            self.desired_frame = create_grid_frame(
                root=self.root, column=1, row=0, style="WhiteBg.TFrame")

            self.S0_SG_T_frame = create_grid_frame(
                root=self.root, column=1, row=1, style="TopWhiteBg.TFrame")

            # Conditions input
            self.initial_conditions_input = initial_conditions_input(
                self.initial_frame)
            self.boundary_conditions_input = boundary_conditions_input(
                self.boundary_frame)
            self.desired_conditions_input = desired_conditions_input(
                self.desired_frame)

            # S0,SG,T info
            # S0
            self.S0_frame = create_grid_frame(
                root=self.S0_SG_T_frame, column=0, row=0, style="WhiteBg.TFrame")

            self.S0_label_frame = create_grid_frame(
                root=self.S0_frame, column=0, row=0, style="WhiteBg.TFrame")
            self.S0_entry_frame = create_grid_frame(
                root=self.S0_frame, column=1, row=0, style="WhiteBg.TFrame")

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
            self.SG_frame = create_grid_frame(
                root=self.S0_SG_T_frame, column=0, row=1, style="WhiteBg.TFrame")

            self.SG_label_frame = create_grid_frame(
                root=self.SG_frame, column=0, row=0, style="WhiteBg.TFrame")
            self.SG_entry_frame = create_grid_frame(
                root=self.SG_frame, column=1, row=0, style="WhiteBg.TFrame")

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
            self.T_frame = create_grid_frame(
                root=self.S0_SG_T_frame, column=0, row=2, style="WhiteBg.TFrame")

            self.T_label_frame = create_grid_frame(
                root=self.T_frame, column=0, row=0, style="WhiteBg.TFrame")
            self.T_entry_frame = create_grid_frame(
                root=self.T_frame, column=1, row=0, style="WhiteBg.TFrame")

            self.T_var = StringVar()
            self.T_var.set("1")

            Label(self.T_label_frame, text="T =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.T_entry = Entry(
                self.T_entry_frame, width=ENTRY_WIDTH, textvariable=self.T_var, state="readonly")
            self.T_entry.grid(column=0, row=0, sticky=(N, E, W, S))
        except Exception as e:
            raise e

    def change_S0_SG_T(self, S0: str, SG: str, T: str):
        try:
            self.S0_var.set(S0)
            self.SG_var.set(SG)
            self.T_var.set(T)
        except Exception as e:
            raise e
