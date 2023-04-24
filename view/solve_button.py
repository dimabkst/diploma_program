from tkinter import *
from tkinter import ttk


class solve_button:

    def __init__(self, root, command):
        try:
            s = ttk.Style()
            s.configure("TopWhiteBg.TFrame", background="white",
                        borderwidth=5, relief='raised')
            s.configure("VectorWhiteBg.TFrame", background="white",
                        borderwidth=5, relief="solid")
            s.configure("WhiteBg.TFrame", background="white")
            s.configure("WhiteBg.TLabel", background="white")

            # Frames
            self.root = ttk.Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.solve_button_frame = ttk.Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.solve_button_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            #

            # Solve button
            self.solve_button = ttk.Button(self.solve_button_frame, text="Розв'язати систему",
                                           command=command)
            self.solve_button.grid(column=1, row=1, sticky=(N, W, E, S))
            #

            # Align
            self.align_rows_cols(self.solve_button_frame)
            self.solve_button_frame.grid_rowconfigure(0, weight=1)
            self.solve_button_frame.grid_rowconfigure(2, weight=1)
            self.solve_button_frame.grid_columnconfigure(2, weight=1)

            self.align_rows_cols(self.root)
            #
        except Exception as e:
            raise e

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
