from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from view.utils import align_rows_cols


class results_output:

    def __init__(self, root):
        try:
            self.solutions = None

            s = ttk.Style()
            s.configure("TopWhiteBg.TFrame", background="white",
                        borderwidth=5, relief='raised')
            s.configure("WhiteBg.TFrame", background="white")
            s.configure("WhiteBg.TLabel", background="white")

            # Frames
            self.root = ttk.Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.results_output_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.results_output_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))
            #

            # Align
            align_rows_cols(self.results_output_frame)
            align_rows_cols(self.root)
            #
        except Exception as e:
            raise e

    def receive_data_and_show_it(self, solutions):
        try:
            # Cleaning everything that was before
            self.clear()

            # Output results
            for i in range(len(solutions)):
                # Data
                solution_plot_data = solutions[i].get("solution_plot_data")
                precision = solutions[i].get("precision")
                Yrl0 = solutions[i].get("Yrl0")
                stock_problem_solution_plot_data = solutions[i].get(
                    "stock_problem_solution_plot_data")

                # Frames
                step_frame = ttk.Frame(
                    self.results_output_frame, style="TopWhiteBg.TFrame", padding="3 3 12 12")
                step_frame.grid(column=0, row=i, sticky=(N, W, E, S))

                solution_step_frame = ttk.Frame(
                    step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                solution_step_frame.grid(column=0, row=0, sticky=(N, W, E, S))

                plot_step_frame = ttk.Frame(
                    solution_step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                plot_step_frame.grid(column=1, row=0, sticky=(N, W, E, S))

                precision_step_frame = ttk.Frame(
                    step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                precision_step_frame.grid(column=1, row=0, sticky=(N, W, E, S))

                Yrl0_step_frame = ttk.Frame(
                    step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                Yrl0_step_frame.grid(column=2, row=0, sticky=(N, W, E, S))

                stock_problem_plot_step_frame = ttk.Frame(
                    solution_step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                stock_problem_plot_step_frame.grid(
                    column=3, row=0, sticky=(N, W, E, S))

                # Place data
                ttk.Label(solution_step_frame, text=f"Розв'язок №{i + 1}", style="WhiteBg.TLabel") \
                    .grid(column=0, row=0, sticky=(N, W, E, S))

                # Plot of solution if exists
                if solution_plot_data:
                    # the figure that will contain the plot
                    step_fig = Figure(figsize=(5, 5), dpi=100)

                    # adding the subplot
                    step_plot = step_fig.add_subplot(111, projection="3d")

                    # plotting the graph
                    step_plot.plot_surface(solution_plot_data['X'], solution_plot_data['T'], solution_plot_data['Y'],
                                           cmap='viridis', edgecolor='none')
                    step_plot.set_title('Графік y(x,t)')
                    step_plot.set_xlabel('X')
                    step_plot.set_ylabel('T')
                    step_plot.set_zlabel('Y')

                    # creating the Tkinter canvas containing the Matplotlib figure
                    step_canvas = FigureCanvasTkAgg(
                        step_fig, master=plot_step_frame)
                    step_canvas.draw()

                    # placing the canvas on the Tkinter window
                    step_canvas.get_tk_widget().pack()

                    # creating the Matplotlib toolbar
                    step_toolbar = NavigationToolbar2Tk(
                        step_canvas, plot_step_frame)
                    step_toolbar.update()

                    # placing the toolbar on the Tkinter window
                    step_canvas.get_tk_widget().pack()
                    #

                ttk.Label(precision_step_frame, text=f"Точність розв'язку №{i + 1} Ɛ²:", style="WhiteBg.TLabel") \
                    .grid(column=0, row=0, sticky=(N, W, E, S))
                ttk.Label(precision_step_frame, text=f"{precision}", style="WhiteBg.TLabel") \
                    .grid(column=1, row=0, sticky=(N, W, E, S))

                ttk.Label(Yrl0_step_frame, text=f"Керуючі Yrl0 ≡ phi №{i + 1}:", style="WhiteBg.TLabel") \
                    .grid(column=0, row=0, sticky=(N, W, E, S))
                ttk.Label(Yrl0_step_frame, text=f"{Yrl0}", style="WhiteBg.TLabel") \
                    .grid(column=1, row=0, sticky=(N, W, E, S))

                # Plot of stock solution if exists
                if stock_problem_solution_plot_data:
                    # the figure that will contain the plot
                    stock_problem_step_fig = Figure(figsize=(5, 5), dpi=100)

                    # adding the subplot
                    stock_problem_step_plot = stock_problem_step_fig.add_subplot(
                        111, projection="3d")

                    # plotting the graph
                    stock_problem_step_plot.plot_surface(stock_problem_solution_plot_data['X'], stock_problem_solution_plot_data['T'], stock_problem_solution_plot_data['Y'],
                                                         cmap='viridis', edgecolor='none')
                    stock_problem_step_plot.set_title(
                        'Графік щільності акцій u(x,t)')
                    stock_problem_step_plot.set_xlabel('X')
                    stock_problem_step_plot.set_ylabel('T')
                    stock_problem_step_plot.set_zlabel('Y')

                    # creating the Tkinter canvas containing the Matplotlib figure
                    stock_problem_step_canvas = FigureCanvasTkAgg(
                        stock_problem_step_fig, master=stock_problem_plot_step_frame)
                    stock_problem_step_canvas.draw()

                    # placing the canvas on the Tkinter window
                    stock_problem_step_canvas.get_tk_widget().pack()

                    # creating the Matplotlib toolbar
                    stock_problem_step_toolbar = NavigationToolbar2Tk(
                        stock_problem_step_canvas, stock_problem_plot_step_frame)
                    stock_problem_step_toolbar.update()

                    # placing the toolbar on the Tkinter window
                    stock_problem_step_canvas.get_tk_widget().pack()
                    #

                # Align
                align_rows_cols(solution_step_frame)

                align_rows_cols(plot_step_frame)

                align_rows_cols(precision_step_frame)

                align_rows_cols(Yrl0_step_frame)

                align_rows_cols(stock_problem_plot_step_frame)

                align_rows_cols(step_frame)

            self.solutions = solutions
            align_rows_cols(self.results_output_frame)
            align_rows_cols(self.root)

        except Exception as e:
            raise e

    def clear(self):
        self.solutions = None
        for child in self.results_output_frame.winfo_children():
            for grandchild in child.winfo_children():
                grandchild.destroy()
