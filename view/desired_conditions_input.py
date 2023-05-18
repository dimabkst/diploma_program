from tkinter import N, E, W, S, StringVar, PhotoImage
from tkinter.ttk import Label, Entry
from view.utils import ENTRY_WIDTH, change_and_show_1dim, change_and_show_2dim_desired, create_grid_frame, create_frame_label_entrie_frames


class desired_conditions_input:

    def __init__(self, root):
        try:
            # Frames
            self.root = create_grid_frame(
                root=root, column=0, row=0, style="TopWhiteBg.TFrame")

            self.desired_frame = create_grid_frame(
                root=self.root, column=0, row=0, style="WhiteBg.TFrame")
            #

            # desired conditions
            self.desired_top_frame = create_grid_frame(
                root=self.desired_frame, column=0, row=0, style="WhiteBg.TFrame")

            self.desired_bot_frame = create_grid_frame(
                root=self.desired_frame, column=0, row=1, style="WhiteBg.TFrame")

            self.desired_top_left_frame = create_grid_frame(
                root=self.desired_top_frame, column=0, row=0, style="WhiteBg.TFrame")

            self.desired_top_right_frame = create_grid_frame(
                root=self.desired_top_frame, column=1, row=0, style="WhiteBg.TFrame")

            # I input
            self.I_frame, self.I_label_frame, self.I_entry_frame = create_frame_label_entrie_frames(
                root=self.desired_top_left_frame, column=0, row=0, isRow=True, style="WhiteBg.TFrame")

            self.I_var = StringVar()
            self.I_var.set("1")
            self.I_var.trace("w", lambda name, index,
                             mode: self.change_and_show_desired())

            Label(self.I_label_frame, text="Кількість операторів Li(dx, dt) I -", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = Entry(
                self.I_entry_frame, width=ENTRY_WIDTH, textvariable=self.I_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Li input
            self.Li_frame, self.Li_label_frame, self.Li_Li_frame = create_frame_label_entrie_frames(
                root=self.desired_top_left_frame, column=0, row=1, isRow=False, style="WhiteBg.TFrame")

            self.Li_labels = []
            self.Li_vars = []
            self.Li_entries = []

            for i in range(int(self.I_var.get() or 0)):
                self.Li_vars.append(StringVar())
                self.Li_vars[i].set("1*d[x,0]")
                self.Li_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_desired())

                self.Li_labels.append(
                    Label(self.Li_Li_frame, text=f"L{i + 1}(dx, dt):", style="WhiteBg.TLabel"))
                self.Li_labels[i].grid(row=i, column=0, sticky=(N, W, E, S))

                self.Li_entries.append(
                    Entry(self.Li_Li_frame, width=ENTRY_WIDTH, textvariable=self.Li_vars[i]))
                self.Li_entries[i].grid(row=i, column=1, sticky=(N, W, E, S))

            Label(self.Li_label_frame, text="Оператори Li(dx, dt):", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Ji input
            self.Ji_frame, self.Ji_label_frame, self.Ji_Ji_frame = create_frame_label_entrie_frames(
                root=self.desired_top_right_frame, column=0, row=0, isRow=False, style="WhiteBg.TFrame")

            self.Ji_labels = []
            self.Ji_vars = []
            self.Ji_entries = []

            Label(self.Ji_label_frame, text="Кількість дискретних точок спостережень Li(dx, dt) Ji -", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))

            for i in range(int(self.I_var.get() or 0)):
                self.Ji_vars.append(StringVar())
                self.Ji_vars[i].set("1")
                self.Ji_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_desired())

                self.Ji_labels.append(Label(self.Ji_Ji_frame, text=f"J{i+1}",
                                            style="WhiteBg.TLabel"))
                self.Ji_labels[i].grid(row=0, column=i, sticky=(N, W, E, S))

                self.Ji_entries.append(
                    Entry(self.Ji_Ji_frame, width=ENTRY_WIDTH, textvariable=self.Ji_vars[i]))
                self.Ji_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))
            #

            # sij input
            self.sij_frame, self.sij_label_frame, self.sij_sij_frame = create_frame_label_entrie_frames(
                root=self.desired_top_right_frame, column=0, row=1, isRow=False, style="WhiteBg.TFrame")

            Label(self.sij_label_frame, text="Дискретні точки спостережень Li(dx, dt), sij є SG x [0, T] у форматі:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            sij_format_image = PhotoImage(file="./assets/sij.gif")
            sij_format_image_label = Label(
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
                        Label(self.sij_sij_frame, text=f"s{i + 1}{j + 1}", style="WhiteBg.TLabel"))
                    self.sij_labels[i][j].grid(
                        row=i, column=j * 2, sticky=(N, W, E, S))

                    self.sij_vars[i].append(StringVar())
                    self.sij_vars[i][j].set("(0,0)")
                    self.sij_vars[i][j].trace(
                        "w", lambda name, index, mode: self.change_and_show_desired())

                    self.sij_entries[i].append(Entry(
                        self.sij_sij_frame, width=ENTRY_WIDTH, textvariable=self.sij_vars[i][j]))
                    self.sij_entries[i][j].grid(
                        row=i, column=j * 2 + 1, sticky=(N, W, E, S))
            #

            # Yij input
            self.yij_frame, self.yij_label_frame, self.yij_yij_frame = create_frame_label_entrie_frames(
                root=self.desired_bot_frame, column=0, row=0, isRow=False, style="WhiteBg.TFrame")

            Label(self.yij_label_frame, text="Бажані спостереження Yij процесу:", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.yij_labels = []
            self.yij_vars = []
            self.yij_entries = []

            for i in range(int(self.I_var.get() or 0)):
                self.yij_labels.append([])
                self.yij_vars.append([])
                self.yij_entries.append([])

                for j in range(int(self.Ji_vars[i].get() or 0)):
                    self.yij_labels[i].append(Label(self.yij_yij_frame,
                                                    text=f"L{i + 1}y(x,t)|(x,t)={self.sij_vars[i][j].get()} "
                                                    f"= Y{i + 1}{j + 1} =", style="WhiteBg.TLabel"))
                    self.yij_labels[i][j].grid(
                        row=i, column=j * 2, sticky=(N, W, E, S))

                    self.yij_vars[i].append(StringVar())
                    self.yij_vars[i][j].set("0")
                    self.yij_vars[i][j].trace(
                        "w", lambda name, index, mode: self.change_and_show_desired())

                    self.yij_entries[i].append(Entry(self.yij_yij_frame, width=ENTRY_WIDTH,
                                                     textvariable=self.yij_vars[i][j]))
                    self.yij_entries[i][j].grid(
                        row=i, column=j * 2 + 1, sticky=(N, W, E, S))

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
