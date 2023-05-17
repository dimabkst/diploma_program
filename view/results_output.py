from tkinter import N, E, W, S
from tkinter.ttk import Frame, Label
from view.utils import align_rows_cols, create_plot


class results_output:

    def __init__(self, root):
        try:
            self.solutions = None

            # Frames
            self.root = Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.results_output_frame = Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.results_output_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))
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
                step_frame = Frame(
                    self.results_output_frame, style="TopWhiteBg.TFrame", padding="3 3 12 12")
                step_frame.grid(column=0, row=i, sticky=(N, W, E, S))

                solution_step_frame = Frame(
                    step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                solution_step_frame.grid(column=0, row=0, sticky=(N, W, E, S))

                plot_step_frame = Frame(
                    solution_step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                plot_step_frame.grid(column=1, row=0, sticky=(N, W, E, S))

                precision_step_frame = Frame(
                    step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                precision_step_frame.grid(column=1, row=0, sticky=(N, W, E, S))

                Yrl0_step_frame = Frame(
                    step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                Yrl0_step_frame.grid(column=2, row=0, sticky=(N, W, E, S))

                stock_problem_plot_step_frame = Frame(
                    solution_step_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
                stock_problem_plot_step_frame.grid(
                    column=3, row=0, sticky=(N, W, E, S))
                #

                # Place data
                Label(solution_step_frame, text=f"Розв'язок №{i + 1}", style="WhiteBg.TLabel") \
                    .grid(column=0, row=0, sticky=(N, W, E, S))

                # Plot of solution if exists
                create_plot(solution_plot_data,
                            'Графік y(x,t)', plot_step_frame)

                Label(precision_step_frame, text=f"Точність розв'язку №{i + 1} Ɛ²:", style="WhiteBg.TLabel") \
                    .grid(column=0, row=0, sticky=(N, W, E, S))
                Label(precision_step_frame, text=f"{precision}", style="WhiteBg.TLabel") \
                    .grid(column=1, row=0, sticky=(N, W, E, S))

                Label(Yrl0_step_frame, text=f"Керуючі Yrl0 ≡ phi №{i + 1}:", style="WhiteBg.TLabel") \
                    .grid(column=0, row=0, sticky=(N, W, E, S))
                Label(Yrl0_step_frame, text=f"{Yrl0}", style="WhiteBg.TLabel") \
                    .grid(column=1, row=0, sticky=(N, W, E, S))

                # Plot of stock solution if exists
                create_plot(
                    stock_problem_solution_plot_data, 'Графік щільності акцій u(x,t)', stock_problem_plot_step_frame)

            self.solutions = solutions

            align_rows_cols(self.root)

        except Exception as e:
            raise e

    def clear(self):
        self.solutions = None
        _clear_for_parent(self.results_output_frame)


def _clear_for_parent(parent):
    for child in parent.winfo_children():
        if len(child.winfo_children()):
            _clear_for_parent(child)

        child.destroy()
