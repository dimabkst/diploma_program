from tkinter import *
from tkinter import ttk
from .initial_conditions_input import initial_conditions_input
from .boundary_conditions_input import boundary_conditions_input

ENTRY_WIDTH = 10

class initial_boundary_conditions_input:

    def __init__(self, root):
        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
        s.configure("WhiteBg.TFrame", background="white")

        # Frames
        self.root = ttk.Frame(root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.root.grid(column=0, row=0, sticky=(N, W, E, S))

        self.initial_frame = ttk.Frame(self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
        self.initial_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.boundary_frame = ttk.Frame(self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
        self.boundary_frame.grid(column=0, row=1, sticky=(N, W, E, S))

        self.initial_conditions_input = initial_conditions_input(self.initial_frame)
        self.boundary_conditions_input = boundary_conditions_input(self.boundary_frame)

        self.align_rows_cols(self.initial_frame)
        self.align_rows_cols(self.boundary_frame)
        self.align_rows_cols(self.root)

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
