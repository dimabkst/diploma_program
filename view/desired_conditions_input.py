from tkinter import *
from tkinter import ttk
from view.utils import align_rows_cols, change_and_show_1dim, change_and_show_2dim_desired

ENTRY_WIDTH = 10


class desired_conditions_input:

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
            self.root.grid()

            self.desired_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.desired_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            #

            # desired conditions
            self.desired_top_frame = ttk.Frame(
                self.desired_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.desired_top_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            self.desired_bot_frame = ttk.Frame(
                self.desired_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.desired_bot_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.desired_top_left_frame = ttk.Frame(
                self.desired_top_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.desired_top_left_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.desired_top_right_frame = ttk.Frame(
                self.desired_top_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.desired_top_right_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            # I input
            self.I_frame = ttk.Frame(
                self.desired_top_left_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.I_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.I_label_frame = ttk.Frame(
                self.I_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.I_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.I_entry_frame = ttk.Frame(
                self.I_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.I_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.I_var = StringVar()
            self.I_var.set("1")
            self.I_var.trace("w", lambda name, index,
                             mode: self.change_and_show_desired())

            ttk.Label(self.I_label_frame, text="Кількість операторів Li(dx, dt) I -", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = ttk.Entry(
                self.I_entry_frame, width=ENTRY_WIDTH, textvariable=self.I_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Li input
            self.Li_frame = ttk.Frame(
                self.desired_top_left_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Li_frame.grid(column=0, row=1, sticky=(N, W, E, S))
            self.Li_label_frame = ttk.Frame(
                self.Li_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Li_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.Li_Li_frame = ttk.Frame(
                self.Li_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Li_Li_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.Li_labels = []
            self.Li_vars = []
            self.Li_entries = []

            for i in range(int(self.I_var.get() or 0)):
                self.Li_vars.append(StringVar())
                self.Li_vars[i].set("1*d[x,0]")
                self.Li_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_desired())

                self.Li_labels.append(
                    ttk.Label(self.Li_Li_frame, text=f"L{i + 1}(dx, dt):", style="WhiteBg.TLabel"))
                self.Li_labels[i].grid(row=i, column=0, sticky=(N, W, E, S))

                self.Li_entries.append(
                    ttk.Entry(self.Li_Li_frame, width=ENTRY_WIDTH, textvariable=self.Li_vars[i]))
                self.Li_entries[i].grid(row=i, column=1, sticky=(N, W, E, S))

            ttk.Label(self.Li_label_frame, text="Оператори Li(dx, dt):", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Ji input
            self.Ji_frame = ttk.Frame(
                self.desired_top_right_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Ji_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.Ji_label_frame = ttk.Frame(
                self.Ji_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Ji_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.Ji_Ji_frame = ttk.Frame(
                self.Ji_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Ji_Ji_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.Ji_labels = []
            self.Ji_vars = []
            self.Ji_entries = []

            ttk.Label(self.Ji_label_frame, text="Кількість дискретних точок спостережень Li(dx, dt) Ji -", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))

            for i in range(int(self.I_var.get() or 0)):
                self.Ji_vars.append(StringVar())
                self.Ji_vars[i].set("1")
                self.Ji_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_desired())

                self.Ji_labels.append(ttk.Label(self.Ji_Ji_frame, text=f"J{i+1}",
                                                style="WhiteBg.TLabel"))
                self.Ji_labels[i].grid(row=0, column=i, sticky=(N, W, E, S))

                self.Ji_entries.append(
                    ttk.Entry(self.Ji_Ji_frame, width=ENTRY_WIDTH, textvariable=self.Ji_vars[i]))
                self.Ji_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))
            #

            # sij input
            self.sij_frame = ttk.Frame(
                self.desired_top_right_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.sij_frame.grid(column=0, row=1, sticky=(N, W, E, S))
            self.sij_label_frame = ttk.Frame(
                self.sij_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.sij_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.sij_sij_frame = ttk.Frame(
                self.sij_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.sij_sij_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            ttk.Label(self.sij_label_frame, text="Дискретні точки спостережень Li(dx, dt), sij є SG x [0, T] у форматі:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            sij_format_image = PhotoImage(file="./assets/sij.gif")
            sij_format_image_label = ttk.Label(
                self.sij_label_frame, image=sij_format_image, style="WhiteBg.TLabel")
            sij_format_image_label.image = sij_format_image
            sij_format_image_label.grid(column=1, row=0, sticky=(N, E, W, S))

            self.sij_labels = []
            self.sij_vars = []
            self.sij_entries = []

            for i in range(int(self.I_var.get() or 0)):
                self.sij_labels.append([])
                self.sij_vars.append([])
                self.sij_entries.append([])

                for j in range(int(self.Ji_vars[i].get() or 0)):
                    self.sij_labels[i].append(
                        ttk.Label(self.sij_sij_frame, text=f"s{i + 1}{j + 1}", style="WhiteBg.TLabel"))
                    self.sij_labels[i][j].grid(
                        row=i, column=j * 2, sticky=(N, W, E, S))

                    self.sij_vars[i].append(StringVar())
                    self.sij_vars[i][j].set("(0,0)")
                    self.sij_vars[i][j].trace(
                        "w", lambda name, index, mode: self.change_and_show_desired())

                    self.sij_entries[i].append(ttk.Entry(
                        self.sij_sij_frame, width=ENTRY_WIDTH, textvariable=self.sij_vars[i][j]))
                    self.sij_entries[i][j].grid(
                        row=i, column=j * 2 + 1, sticky=(N, W, E, S))
            #

            # Yij input
            self.yij_frame = ttk.Frame(
                self.desired_bot_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yij_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.yij_label_frame = ttk.Frame(
                self.yij_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yij_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.yij_yij_frame = ttk.Frame(
                self.yij_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yij_yij_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            ttk.Label(self.yij_label_frame, text="Бажані спостереження Yij процесу:", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.yij_labels = []
            self.yij_vars = []
            self.yij_entries = []

            for i in range(int(self.I_var.get() or 0)):
                self.yij_labels.append([])
                self.yij_vars.append([])
                self.yij_entries.append([])

                for j in range(int(self.Ji_vars[i].get() or 0)):
                    self.yij_labels[i].append(ttk.Label(self.yij_yij_frame,
                                                        text=f"L{i + 1}y(x,t)|(x,t)={self.sij_vars[i][j].get()} "
                                                        f"= Y{i + 1}{j + 1} =", style="WhiteBg.TLabel"))
                    self.yij_labels[i][j].grid(
                        row=i, column=j * 2, sticky=(N, W, E, S))

                    self.yij_vars[i].append(StringVar())
                    self.yij_vars[i][j].set("0")
                    self.yij_vars[i][j].trace(
                        "w", lambda name, index, mode: self.change_and_show_desired())

                    self.yij_entries[i].append(ttk.Entry(self.yij_yij_frame, width=ENTRY_WIDTH,
                                                         textvariable=self.yij_vars[i][j]))
                    self.yij_entries[i][j].grid(
                        row=i, column=j * 2 + 1, sticky=(N, W, E, S))

            # Align everything
            align_rows_cols(self.I_label_frame)
            align_rows_cols(self.I_entry_frame)
            align_rows_cols(self.I_frame)

            align_rows_cols(self.Li_frame)
            align_rows_cols(self.Li_label_frame)
            align_rows_cols(self.Li_Li_frame)

            align_rows_cols(self.Ji_label_frame)
            align_rows_cols(self.Ji_Ji_frame)
            align_rows_cols(self.Ji_frame)

            align_rows_cols(self.sij_frame)
            align_rows_cols(self.sij_label_frame)
            align_rows_cols(self.sij_sij_frame)

            align_rows_cols(self.desired_top_left_frame)
            align_rows_cols(self.desired_top_right_frame)
            align_rows_cols(self.desired_top_frame)

            align_rows_cols(self.yij_frame)
            align_rows_cols(self.yij_label_frame)
            align_rows_cols(self.yij_yij_frame)

            align_rows_cols(self.desired_bot_frame)

            align_rows_cols(self.desired_frame)

            align_rows_cols(self.root)
            #
        except Exception as e:
            raise e

    def change_and_show_desired(self):
        try:
            def new_vars_callback(name, index, mode):
                self.change_and_show_desired()

            self.Li_vars, self.Li_labels, self.Li_entries = change_and_show_1dim(self.I_var,
                                                                                 self.Li_vars, new_vars_callback, lambda i: "1*d[x,0]",
                                                                                 self.Li_labels, lambda i: f"L{i + 1}(dx, dt):", "WhiteBg.TLabel",
                                                                                 self.Li_entries, ENTRY_WIDTH, "normal",
                                                                                 self.Li_Li_frame,
                                                                                 isRow=True)

            self.Ji_vars, self.Ji_labels, self.Ji_entries = change_and_show_1dim(self.I_var,
                                                                                 self.Ji_vars, new_vars_callback, lambda i: "1",
                                                                                 self.Ji_labels, lambda i: f"J{i+1}", "WhiteBg.TLabel",
                                                                                 self.Ji_entries, ENTRY_WIDTH, "normal",
                                                                                 self.Ji_Ji_frame,
                                                                                 isRow=False)

            self.sij_vars, self.sij_labels, self.sij_entries = change_and_show_2dim_desired(self.I_var, self.Ji_vars,
                                                                                            self.sij_vars, new_vars_callback, lambda i, j: "(0,0)",
                                                                                            self.sij_labels, lambda i, j: f"s{i + 1}{j + 1}", "WhiteBg.TLabel",
                                                                                            self.sij_entries, ENTRY_WIDTH, "normal",
                                                                                            self.sij_sij_frame,
                                                                                            additional_conditions=all([el.get() for el in self.Li_vars]))

            self.yij_vars, self.yij_labels, self.yij_entries = change_and_show_2dim_desired(self.I_var, self.Ji_vars,
                                                                                            self.yij_vars, new_vars_callback, lambda i, j: "0",
                                                                                            self.yij_labels, lambda i, j: f"L{i + 1}y(x,t)|(x,t)={self.sij_vars[i][j].get()} = Y{i + 1}{j + 1} =", "WhiteBg.TLabel",
                                                                                            self.yij_entries, ENTRY_WIDTH, "normal",
                                                                                            self.yij_yij_frame,
                                                                                            additional_conditions=all(
                                                                                                [el.get() for el in self.Li_vars])
                                                                                            and all([all([el.get() for el in row]) for row in self.sij_vars]))
        except Exception as e:
            raise e
