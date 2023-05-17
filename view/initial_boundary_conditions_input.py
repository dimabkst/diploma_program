from tkinter import N, E, W, S
from tkinter.ttk import Frame
from .initial_conditions_input import initial_conditions_input
from .boundary_conditions_input import boundary_conditions_input


class initial_boundary_conditions_input:

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

            self.initial_conditions_input = initial_conditions_input(
                self.initial_frame)
            self.boundary_conditions_input = boundary_conditions_input(
                self.boundary_frame)
        except Exception as e:
            raise e
