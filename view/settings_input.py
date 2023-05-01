from tkinter import *
from tkinter import ttk

ENTRY_WIDTH = 10


class settings_input:

    def __init__(self, root):
        try:
            s = ttk.Style()
            s.configure("TopWhiteBg.TFrame", background="white",
                        borderwidth=5, relief='raised')
            s.configure("WhiteBg.TFrame", background="white")
            s.configure("WhiteBg.TLabel", background="white")

            # Frames
            self.root = ttk.Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.integrals_precision_frame = ttk.Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.integrals_precision_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.plot_grid_dimension_frame = ttk.Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.plot_grid_dimension_frame.grid(
                column=0, row=1, sticky=(N, W, E, S))

            # integrals_precision_input
            self.integrals_precision_label_frame = ttk.Frame(
                self.integrals_precision_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.integrals_precision_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.integrals_precision_entry_frame = ttk.Frame(
                self.integrals_precision_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.integrals_precision_entry_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            ttk.Label(self.integrals_precision_label_frame, text="Точність обчислення інтегралів - ", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.integrals_precision_var = StringVar()
            self.integrals_precision_var.set("1.5e-3")

            self.integrals_precision_entry = ttk.Entry(
                self.integrals_precision_entry_frame, width=ENTRY_WIDTH, textvariable=self.integrals_precision_var)
            self.integrals_precision_entry.grid(
                column=0, row=0, sticky=(N, E, W, S))
            #

            # plot_grid_dimension_input
            self.plot_grid_dimension_label_frame = ttk.Frame(
                self.plot_grid_dimension_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.plot_grid_dimension_label_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.plot_grid_dimension_entry_frame = ttk.Frame(
                self.plot_grid_dimension_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.plot_grid_dimension_entry_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            ttk.Label(self.plot_grid_dimension_label_frame, text="Розмірність сітки графіка - ", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.plot_grid_dimension_var = StringVar()
            self.plot_grid_dimension_var.set("20")

            self.plot_grid_dimension_entry = ttk.Entry(
                self.plot_grid_dimension_entry_frame, width=ENTRY_WIDTH, textvariable=self.plot_grid_dimension_var)
            self.plot_grid_dimension_entry.grid(
                column=0, row=0, sticky=(N, E, W, S))
            #

            # Align everything
            self.align_rows_cols(self.integrals_precision_frame)
            self.align_rows_cols(self.integrals_precision_label_frame)
            self.align_rows_cols(self.integrals_precision_entry_frame)

            self.align_rows_cols(self.plot_grid_dimension_frame)
            self.align_rows_cols(self.plot_grid_dimension_label_frame)
            self.align_rows_cols(self.plot_grid_dimension_entry_frame)

            self.align_rows_cols(self.root)
        except Exception as e:
            raise e

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
