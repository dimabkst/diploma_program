from tkinter import *
from tkinter import ttk
from .boundary_conditions_input import boundary_conditions_input
from .desired_conditions_input import desired_conditions_input
from view.utils import align_rows_cols

ENTRY_WIDTH = 10


class boundary_desired_conditions_input:

    def __init__(self, root):
        try:
            s = ttk.Style()
            s.configure("TopWhiteBg.TFrame", background="white",
                        borderwidth=5, relief='raised')
            s.configure("WhiteBg.TFrame", background="white")

            # Frames
            self.root = ttk.Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.boundary_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.boundary_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            self.desired_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.desired_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.boundary_conditions_input = boundary_conditions_input(
                self.boundary_frame)
            self.desired_conditions_input = desired_conditions_input(
                self.desired_frame)

            align_rows_cols(self.boundary_frame)
            align_rows_cols(self.desired_frame)
            align_rows_cols(self.root)
        except Exception as e:
            raise e
