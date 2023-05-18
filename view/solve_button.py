from tkinter import N, E, W, S, messagebox, BooleanVar
from tkinter.ttk import Button, Checkbutton
from view.utils import create_grid_frame


class solve_button:

    def __init__(self, root, command):
        try:
            self.solve_button_command = command

            # Frames
            self.root = create_grid_frame(
                root=root, column=0, row=0, style="TopWhiteBg.TFrame")

            self.solve_button_frame = create_grid_frame(
                root=self.root, column=0, row=0, style="WhiteBg.TFrame")

            self.check_buttons_frame = create_grid_frame(
                root=self.root, column=1, row=0, style="WhiteBg.TFrame")
            #

            # Solve button
            self.solve_button = Button(self.solve_button_frame, text="Розв'язати систему",
                                       command=self.solve_button_callback)
            self.solve_button.grid(column=1, row=1, sticky=(N, W, E, S))
            #

            # Check buttons
            self.plot_var = BooleanVar()
            self.plot_check_button = Checkbutton(
                self.check_buttons_frame, text='Побудувати графік', variable=self.plot_var, style='WhiteBg.TCheckbutton', command=self.check_buttons_callback)
            self.plot_check_button.grid(column=0, row=0, sticky=(N, W, S))

            self.plot_stock_var = BooleanVar()
            self.plot_stock_check_button = Checkbutton(
                self.check_buttons_frame, text='Побудувати графік задачі акцій', variable=self.plot_stock_var, style='WhiteBg.TCheckbutton', command=self.check_buttons_callback)
            self.plot_stock_check_button.grid(
                column=1, row=0, sticky=(N, W, S))

            # Align
            self.solve_button_frame.grid_rowconfigure(0, weight=1)
            self.solve_button_frame.grid_rowconfigure(2, weight=1)
            self.solve_button_frame.grid_columnconfigure(0, weight=1)
            self.solve_button_frame.grid_columnconfigure(2, weight=1)
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
