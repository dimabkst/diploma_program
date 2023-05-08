from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view.utils import align_rows_cols


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

            self.solve_button_command = command

            # Frames
            self.root = ttk.Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.solve_button_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.solve_button_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            self.check_buttons_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.check_buttons_frame.grid(column=1, row=0, sticky=(N, W, E, S))
            #

            # Solve button
            self.solve_button = ttk.Button(self.solve_button_frame, text="Розв'язати систему",
                                           command=self.solve_button_callback)
            self.solve_button.grid(column=1, row=1, sticky=(N, W, E, S))
            #

            # Check buttons
            checkbutton_style = ttk.Style()
            checkbutton_style.configure(
                'WhiteBg.TCheckbutton', background='white')

            self.plot_var = BooleanVar()
            self.plot_check_button = ttk.Checkbutton(
                self.check_buttons_frame, text='Побудувати графік', variable=self.plot_var, style='WhiteBg.TCheckbutton', command=self.check_buttons_callback)
            self.plot_check_button.grid(column=0, row=0, sticky=(N, W, S))

            self.plot_stock_var = BooleanVar()
            self.plot_stock_check_button = ttk.Checkbutton(
                self.check_buttons_frame, text='Побудувати графік задачі акцій', variable=self.plot_stock_var, style='WhiteBg.TCheckbutton', command=self.check_buttons_callback)
            self.plot_stock_check_button.grid(
                column=1, row=0, sticky=(N, W, S))

            # Align
            align_rows_cols(self.solve_button_frame)
            self.solve_button_frame.grid_rowconfigure(0, weight=1)
            self.solve_button_frame.grid_rowconfigure(2, weight=1)
            self.solve_button_frame.grid_columnconfigure(0, weight=1)
            self.solve_button_frame.grid_columnconfigure(2, weight=1)

            align_rows_cols(self.check_buttons_frame)

            align_rows_cols(self.root)
            #
        except Exception as e:
            raise e

    def solve_button_callback(self):
        try:
            self.solve_button_command(
                self.plot_var.get(), self.plot_stock_var.get())
        except Exception as e:
            raise e

    def check_buttons_callback(self):
        try:
            if self.plot_var.get() and self.plot_stock_var.get():
                messagebox.showinfo(
                    'Вказівка', 'Якщо обрати обидві опції, для побудови другого графіку будуть використані дані першого, що може привести до не зовсім очікуваних меж осей.')
        except Exception as e:
            raise e
