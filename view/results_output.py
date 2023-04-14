from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np


class results_output:

    def __init__(self, root):
        try:
            s = ttk.Style()
            s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
            s.configure("WhiteBg.TFrame", background="white")
            s.configure("WhiteBg.TLabel", background="white")

            # Frames
            self.root = ttk.Frame(root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.results_output_frame = ttk.Frame(self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.results_output_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            #

            # Align
            self.align_rows_cols(self.results_output_frame)
            self.align_rows_cols(self.root)
            #
        except Exception as e:
            raise e

    def receive_data_and_show_it(self, solutions):
        try:
            # Cleaning everything that was before
            for child in self.results_output_frame.winfo_children():
                for grandchild in child.winfo_children():
                    grandchild.destroy()

            # Output results
            for i in range(len(solutions)):
                solution = solutions[i]["solution"]
                precision = solutions[i]["precision"]

                step_frame = ttk.Frame(self.results_output_frame, style="TopWhiteBg.TFrame", padding="3 3 12 12")
                step_frame.grid(column=0, row=i, sticky=(N, W, E, S))

                solution_step_frame = ttk.Frame(step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                solution_step_frame.grid(column=0, row=0, sticky=(N, W, E, S))

                plot_step_frame = ttk.Frame(solution_step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                plot_step_frame.grid(column=1, row=0, sticky=(N, W, E, S))

                precision_step_frame = ttk.Frame(step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                precision_step_frame.grid(column=1, row=0, sticky=(N, W, E, S))

                ttk.Label(precision_step_frame, text=f"Точність розв'язку №{i + 1} Ɛ²:", style="WhiteBg.TLabel") \
                    .grid(column=0, row=0, sticky=(N, W, E, S))
                ttk.Label(precision_step_frame, text=f"{precision}", style="WhiteBg.TLabel") \
                    .grid(column=1, row=0, sticky=(N, W, E, S))

                ttk.Label(solution_step_frame, text=f"Розв'язок №{i + 1}", style="WhiteBg.TLabel") \
                    .grid(column=0, row=0, sticky=(N, W, E, S))
                # ttk.Label(solution_step_frame, text=f"{solution}", style="WhiteBg.TLabel") \
                #     .grid(column=1, row=0, sticky=(N, W, E, S))

                # Plot of solution
                # the figure that will contain the plot
                step_fig = Figure(figsize=(5, 5), dpi=100)
                # adding the subplot
                step_plot = step_fig.add_subplot(111, projection="3d")
                # plotting the graph
                x_values = np.arange(-1.0, 1.0, 0.05)
                t_values = np.arange(-1.0, 1.0, 0.05)

                X_values, T_values = np.meshgrid(x_values, t_values)
                Y_values = [[solution(x_value, t_value) for t_value in t_values] for x_value in x_values]
                Y_values = np.array(Y_values)
                step_plot.plot_surface(X_values, T_values, Y_values, rstride=1, cstride=1,
                                       cmap='viridis', edgecolor='none')

                # creating the Tkinter canvas containing the Matplotlib figure
                step_canvas = FigureCanvasTkAgg(step_fig, master=plot_step_frame)
                step_canvas.draw()

                # placing the canvas on the Tkinter window
                step_canvas.get_tk_widget().pack()

                # creating the Matplotlib toolbar
                step_toolbar = NavigationToolbar2Tk(step_canvas, plot_step_frame)
                step_toolbar.update()

                # placing the toolbar on the Tkinter window
                step_canvas.get_tk_widget().pack()
                #

                self.align_rows_cols(solution_step_frame)
                self.align_rows_cols(solution_step_frame)

                self.align_rows_cols(precision_step_frame)
                self.align_rows_cols(precision_step_frame)

                self.align_rows_cols(step_frame)

            self.align_rows_cols(self.results_output_frame)
            self.align_rows_cols(self.root)
        except Exception as e:
            raise e

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
