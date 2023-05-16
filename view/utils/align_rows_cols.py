from tkinter import Toplevel
from tkinter.ttk import Frame, Notebook


def align_rows_cols(main_frame):
    try:
        for frame in main_frame.winfo_children():
            if isinstance(frame, Frame) or isinstance(frame, Toplevel) or isinstance(frame, Notebook):
                align_rows_cols(frame)

                cols_num, rows_num = frame.grid_size()
                for i in range(rows_num):
                    frame.grid_rowconfigure(i, weight=1)
                for j in range(cols_num):
                    frame.grid_columnconfigure(j, weight=1)

        cols_num, rows_num = main_frame.grid_size()
        for i in range(rows_num):
            main_frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            main_frame.grid_columnconfigure(j, weight=1)
    except Exception as e:
        raise e
