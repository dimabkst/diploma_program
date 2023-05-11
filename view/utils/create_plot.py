from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


def create_plot(plot_data: dict, plot_title: str, plot_frame: Frame):
    try:
        if plot_data:
            # the figure that will contain the plot
            fig = Figure(figsize=(5, 5), dpi=100)

            # adding the subplot
            plot = fig.add_subplot(111, projection="3d")

            # plotting the graph
            plot.plot_surface(plot_data['X'], plot_data['T'], plot_data['Y'],
                              cmap='viridis', edgecolor='none')
            plot.set_title(plot_title)
            plot.set_xlabel('X')
            plot.set_ylabel('T')
            plot.set_zlabel('Y')

            plot_data_desired_values = plot_data.get(
                'desired_values')
            if plot_data_desired_values:
                plot.scatter(
                    plot_data_desired_values['X'],
                    plot_data_desired_values['T'],
                    plot_data_desired_values['Y'],
                    c='r',
                    alpha=1)

            # creating the Tkinter canvas containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(
                fig, master=plot_frame)
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()

            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(
                canvas, plot_frame)
            toolbar.update()

            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()
            #
    except Exception as e:
        raise e
