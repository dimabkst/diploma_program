from tkinter import N, E, W, S, StringVar
from tkinter.ttk import Label, Entry
from view.utils import ENTRY_WIDTH, change_and_show_1dim, change_and_show_2dim, create_grid_frame, create_frame_label_entrie_frames


class initial_conditions_input:

    def __init__(self, root):
        try:
            # Frames
            self.root = create_grid_frame(
                root=root, column=0, row=0, style="TopWhiteBg.TFrame")

            self.initial_frame = create_grid_frame(
                root=self.root, column=0, row=0, style="WhiteBg.TFrame")
            #

            # Initial conditions
            self.initial_top_frame = create_grid_frame(
                root=self.initial_frame, column=0, row=0, style="WhiteBg.TFrame")

            self.initial_bot_frame = create_grid_frame(
                root=self.initial_frame, column=0, row=1, style="WhiteBg.TFrame")

            self.initial_top_left_frame = create_grid_frame(
                root=self.initial_top_frame, column=0, row=0, style="WhiteBg.TFrame")

            self.initial_top_right_frame = create_grid_frame(
                root=self.initial_top_frame, column=1, row=0, style="WhiteBg.TFrame")

            # R0 input
            self.R0_frame, self.R0_label_frame, self.R0_entry_frame = create_frame_label_entrie_frames(
                root=self.initial_top_left_frame, column=0, row=0, isRow=True, style="WhiteBg.TFrame")

            self.R0_var = StringVar()
            self.R0_var.set("1")
            self.R0_var.trace("w", lambda name, index,
                              mode: self.change_and_show_initial())

            Label(self.R0_label_frame, text="Кількість початкових операторів Lr0(dt) R0 -", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = Entry(
                self.R0_entry_frame, width=ENTRY_WIDTH, textvariable=self.R0_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Lr0 input
            self.Lr0_frame, self.Lr0_label_frame, self.Lr0_Lr0_frame = create_frame_label_entrie_frames(
                root=self.initial_top_left_frame, column=0, row=1, isRow=False, style="WhiteBg.TFrame")

            self.Lr0_labels = []
            self.Lr0_vars = []
            self.Lr0_entries = []

            for i in range(int(self.R0_var.get() or 0)):
                self.Lr0_vars.append(StringVar())
                self.Lr0_vars[i].set("1*d[t,0]")
                self.Lr0_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_initial())

                self.Lr0_labels.append(
                    Label(self.Lr0_Lr0_frame, text=f"L{i + 1}0(dt):", style="WhiteBg.TLabel"))
                self.Lr0_labels[i].grid(row=i, column=0, sticky=(N, W, E, S))

                self.Lr0_entries.append(Entry(
                    self.Lr0_Lr0_frame, width=ENTRY_WIDTH, textvariable=self.Lr0_vars[i]))
                self.Lr0_entries[i].grid(row=i, column=1, sticky=(N, W, E, S))

            Label(self.Lr0_label_frame, text="Початкові оператори Lr0(dt):", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # L0 input
            self.L0_frame, self.L0_label_frame, self.L0_entry_frame = create_frame_label_entrie_frames(
                root=self.initial_top_right_frame, column=0, row=0, isRow=True, style="WhiteBg.TFrame")

            self.L0_var = StringVar()
            self.L0_var.set("1")
            self.L0_var.trace("w", lambda name, index,
                              mode: self.change_and_show_initial())

            Label(self.L0_label_frame, text="Кількість дискретних точок спостережень Lr0(dt) L0 -",
                  style="WhiteBg.TLabel").grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = Entry(
                self.L0_entry_frame, width=ENTRY_WIDTH, textvariable=self.L0_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # xl0 input
            self.xl0_frame, self.xl0_label_frame, self.xl0_xl0_frame = create_frame_label_entrie_frames(
                root=self.initial_top_right_frame, column=0, row=1, isRow=False, style="WhiteBg.TFrame")

            self.xl0_labels = []
            self.xl0_vars = []
            self.xl0_entries = []

            for i in range(int(self.L0_var.get() or 0)):
                self.xl0_vars.append(StringVar())
                self.xl0_vars[i].set("1")
                self.xl0_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_initial())

                self.xl0_labels.append(
                    Label(self.xl0_xl0_frame, text=f"x{i + 1}0", style="WhiteBg.TLabel"))
                self.xl0_labels[i].grid(row=0, column=i, sticky=(N, W, E, S))

                self.xl0_entries.append(Entry(
                    self.xl0_xl0_frame, width=ENTRY_WIDTH, textvariable=self.xl0_vars[i]))
                self.xl0_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))

            Label(self.xl0_label_frame, text="Дискретні точки спостережень Lr0(dt), xl0 є S0:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Yrl0 input
            self.yrl0_frame, self.yrl0_label_frame, self.yrl0_yrl0_frame = create_frame_label_entrie_frames(
                root=self.initial_bot_frame, column=0, row=0, isRow=False, style="WhiteBg.TFrame")

            Label(self.yrl0_label_frame, text="Початкові спостереження Yrl0 процесу:", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.yrl0_labels = []
            self.yrl0_vars = []
            self.yrl0_entries = []

            for r in range(int(self.R0_var.get() or 0)):
                self.yrl0_labels.append([])
                self.yrl0_vars.append([])
                self.yrl0_entries.append([])

                for l in range(int(self.L0_var.get() or 0)):
                    self.yrl0_labels[r].append(Label(self.yrl0_yrl0_frame,
                                                     text=f"L{r + 1}0y(x,t)|(x={self.xl0_vars[l].get()},t=0) "
                                                     f"= Y{r + 1}{l + 1}0 =", style="WhiteBg.TLabel"))
                    self.yrl0_labels[r][l].grid(
                        row=r, column=l * 2, sticky=(N, W, E, S))

                    self.yrl0_vars[r].append(StringVar())
                    self.yrl0_vars[r][l].set(f'phi{r + 1}{l + 1}')
                    self.yrl0_vars[r][l].trace(
                        "w", lambda name, index, mode: self.change_and_show_initial())

                    self.yrl0_entries[r].append(Entry(self.yrl0_yrl0_frame, width=ENTRY_WIDTH,
                                                      textvariable=self.yrl0_vars[r][l], state="readonly"))
                    self.yrl0_entries[r][l].grid(
                        row=r, column=l * 2 + 1, sticky=(N, W, E, S))
            #
        except Exception as e:
            raise e

    def change_and_show_initial(self):
        try:
            def new_vars_callback(name, index, mode):
                self.change_and_show_initial()

            self.Lr0_vars, self.Lr0_labels, self.Lr0_entries = change_and_show_1dim(self.R0_var,
                                                                                    self.Lr0_vars, new_vars_callback, lambda i: "1*d[t,0]",
                                                                                    self.Lr0_labels, lambda i: f"L{i + 1}0(dt):", "WhiteBg.TLabel",
                                                                                    self.Lr0_entries, ENTRY_WIDTH, "normal",
                                                                                    self.Lr0_Lr0_frame,
                                                                                    isRow=True)

            self.xl0_vars, self.xl0_labels, self.xl0_entries = change_and_show_1dim(self.L0_var,
                                                                                    self.xl0_vars, new_vars_callback, lambda i: "1",
                                                                                    self.xl0_labels, lambda i: f"x{i + 1}0", "WhiteBg.TLabel",
                                                                                    self.xl0_entries, ENTRY_WIDTH, "normal",
                                                                                    self.xl0_xl0_frame,
                                                                                    isRow=False)

            self.yrl0_vars, self.yrl0_labels, self.yrl0_entries = change_and_show_2dim(self.R0_var, self.L0_var,
                                                                                       self.yrl0_vars, lambda i, j: f'phi{i + 1}{j + 1}',
                                                                                       self.yrl0_labels, lambda i, j: f"L{i + 1}0y(x,t)|(x={self.xl0_vars[j].get()},t=0) = Y{i + 1}{j + 1}0 =", "WhiteBg.TLabel",
                                                                                       self.yrl0_entries, ENTRY_WIDTH, "readonly",
                                                                                       self.yrl0_yrl0_frame,
                                                                                       additional_conditions=all([el.get() for el in self.Lr0_vars]) and all([el.get() for el in self.xl0_vars]))
        except Exception as e:
            raise e
