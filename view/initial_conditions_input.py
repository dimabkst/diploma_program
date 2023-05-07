from tkinter import *
from tkinter import ttk

ENTRY_WIDTH = 10


class initial_conditions_input:

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

            self.initial_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.initial_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            #

            # Initial conditions
            self.initial_top_frame = ttk.Frame(
                self.initial_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.initial_top_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            self.initial_bot_frame = ttk.Frame(
                self.initial_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.initial_bot_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.initial_top_left_frame = ttk.Frame(
                self.initial_top_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.initial_top_left_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.initial_top_right_frame = ttk.Frame(
                self.initial_top_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.initial_top_right_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            # R0 input
            self.R0_frame = ttk.Frame(
                self.initial_top_left_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.R0_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.R0_label_frame = ttk.Frame(
                self.R0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.R0_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.R0_entry_frame = ttk.Frame(
                self.R0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.R0_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.R0_var = StringVar()
            self.R0_var.set("1")
            self.R0_var.trace("w", lambda name, index,
                              mode: self.change_and_show_initial())

            ttk.Label(self.R0_label_frame, text="Кількість початкових операторів Lr0(dt) R0 -", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = ttk.Entry(
                self.R0_entry_frame, width=ENTRY_WIDTH, textvariable=self.R0_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Lr0 input
            self.Lr0_frame = ttk.Frame(
                self.initial_top_left_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Lr0_frame.grid(column=0, row=1, sticky=(N, W, E, S))
            self.Lr0_label_frame = ttk.Frame(
                self.Lr0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Lr0_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.Lr0_Lr0_frame = ttk.Frame(
                self.Lr0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.Lr0_Lr0_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.Lr0_labels = []
            self.Lr0_vars = []
            self.Lr0_entries = []

            for i in range(int(self.R0_var.get() or 0)):
                self.Lr0_vars.append(StringVar())
                self.Lr0_vars[i].set("1*d[t,0]")
                self.Lr0_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_initial())

                self.Lr0_labels.append(
                    ttk.Label(self.Lr0_Lr0_frame, text=f"L{i + 1}0(dt):", style="WhiteBg.TLabel"))
                self.Lr0_labels[i].grid(row=i, column=0, sticky=(N, W, E, S))

                self.Lr0_entries.append(ttk.Entry(
                    self.Lr0_Lr0_frame, width=ENTRY_WIDTH, textvariable=self.Lr0_vars[i]))
                self.Lr0_entries[i].grid(row=i, column=1, sticky=(N, W, E, S))

            ttk.Label(self.Lr0_label_frame, text="Початкові оператори Lr0(dt):", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # L0 input
            self.L0_frame = ttk.Frame(
                self.initial_top_right_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.L0_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.L0_label_frame = ttk.Frame(
                self.L0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.L0_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.L0_entry_frame = ttk.Frame(
                self.L0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.L0_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.L0_var = StringVar()
            self.L0_var.set("1")
            self.L0_var.trace("w", lambda name, index,
                              mode: self.change_and_show_initial())

            ttk.Label(self.L0_label_frame, text="Кількість дискретних точок спостережень Lr0(dt) L0 -",
                      style="WhiteBg.TLabel").grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = ttk.Entry(
                self.L0_entry_frame, width=ENTRY_WIDTH, textvariable=self.L0_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # xl0 input
            self.xl0_frame = ttk.Frame(
                self.initial_top_right_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.xl0_frame.grid(column=0, row=1, sticky=(N, W, E, S))
            self.xl0_label_frame = ttk.Frame(
                self.xl0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.xl0_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.xl0_xl0_frame = ttk.Frame(
                self.xl0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.xl0_xl0_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.xl0_labels = []
            self.xl0_vars = []
            self.xl0_entries = []

            for i in range(int(self.L0_var.get() or 0)):
                self.xl0_vars.append(StringVar())
                self.xl0_vars[i].set("1")
                self.xl0_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_initial())

                self.xl0_labels.append(
                    ttk.Label(self.xl0_xl0_frame, text=f"x{i + 1}0", style="WhiteBg.TLabel"))
                self.xl0_labels[i].grid(row=0, column=i, sticky=(N, W, E, S))

                self.xl0_entries.append(ttk.Entry(
                    self.xl0_xl0_frame, width=ENTRY_WIDTH, textvariable=self.xl0_vars[i]))
                self.xl0_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))

            ttk.Label(self.xl0_label_frame, text="Дискретні точки спостережень Lr0(dt), xl0 є S0:", style="WhiteBg.TLabel")\
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Yrl0 input
            self.yrl0_frame = ttk.Frame(
                self.initial_bot_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yrl0_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.yrl0_label_frame = ttk.Frame(
                self.yrl0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yrl0_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.yrl0_yrl0_frame = ttk.Frame(
                self.yrl0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yrl0_yrl0_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            ttk.Label(self.yrl0_label_frame, text="Початкові спостереження Yrl0 процесу:", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.yrl0_labels = []
            self.yrl0_vars = []
            self.yrl0_entries = []

            for r in range(int(self.R0_var.get() or 0)):
                self.yrl0_labels.append([])
                self.yrl0_vars.append([])
                self.yrl0_entries.append([])

                for l in range(int(self.L0_var.get() or 0)):
                    self.yrl0_labels[r].append(ttk.Label(self.yrl0_yrl0_frame,
                                                         text=f"L{r + 1}0y(x,t)|(x={self.xl0_vars[l].get()},t=0) "
                                                         f"= Y{r + 1}{l + 1}0 =", style="WhiteBg.TLabel"))
                    self.yrl0_labels[r][l].grid(
                        row=r, column=l * 2, sticky=(N, W, E, S))

                    self.yrl0_vars[r].append(StringVar())
                    self.yrl0_vars[r][l].set(f'phi{r + 1}{l + 1}')
                    self.yrl0_vars[r][l].trace(
                        "w", lambda name, index, mode: self.change_and_show_initial())

                    self.yrl0_entries[r].append(ttk.Entry(self.yrl0_yrl0_frame, width=ENTRY_WIDTH,
                                                          textvariable=self.yrl0_vars[r][l], state="readonly"))
                    self.yrl0_entries[r][l].grid(
                        row=r, column=l * 2 + 1, sticky=(N, W, E, S))
            #

            # Align everything
            self.align_rows_cols(self.R0_label_frame)
            self.align_rows_cols(self.R0_entry_frame)
            self.align_rows_cols(self.R0_frame)

            self.align_rows_cols(self.Lr0_frame)
            self.align_rows_cols(self.Lr0_label_frame)
            self.align_rows_cols(self.Lr0_Lr0_frame)

            self.align_rows_cols(self.L0_label_frame)
            self.align_rows_cols(self.L0_entry_frame)
            self.align_rows_cols(self.L0_frame)

            self.align_rows_cols(self.xl0_frame)
            self.align_rows_cols(self.xl0_label_frame)
            self.align_rows_cols(self.xl0_xl0_frame)

            self.align_rows_cols(self.initial_top_left_frame)
            self.align_rows_cols(self.initial_top_right_frame)
            self.align_rows_cols(self.initial_top_frame)

            self.align_rows_cols(self.yrl0_frame)
            self.align_rows_cols(self.yrl0_label_frame)
            self.align_rows_cols(self.yrl0_yrl0_frame)

            self.align_rows_cols(self.initial_bot_frame)

            self.align_rows_cols(self.initial_frame)

            self.align_rows_cols(self.root)
            #
        except Exception as e:
            raise e

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)

    def change_and_show_Lr0(self):
        try:
            if self.R0_var.get() and int(self.R0_var.get()) > 0:
                old_count = len(self.Lr0_vars)
                for i in range(max(old_count, int(self.R0_var.get() or 0))):
                    if i >= min(old_count, int(self.R0_var.get() or 0)):
                        if old_count > int(self.R0_var.get() or 0):
                            self.Lr0_vars = self.Lr0_vars[0:i]

                            for ii in range(i, old_count):
                                self.Lr0_labels[ii].destroy()
                                self.Lr0_entries[ii].destroy()

                            self.Lr0_labels = self.Lr0_labels[0:i]
                            self.Lr0_entries = self.Lr0_entries[0:i]
                            break
                        else:
                            self.Lr0_vars.append(StringVar())

                            self.Lr0_labels.append(
                                ttk.Label(self.Lr0_Lr0_frame, text=f"L{i + 1}0(dt):", style="WhiteBg.TLabel"))
                            self.Lr0_entries.append(
                                ttk.Entry(self.Lr0_Lr0_frame, width=ENTRY_WIDTH,
                                          textvariable=self.Lr0_vars[i]))

                            self.Lr0_vars[i].set("1*d[t,0]")
                            self.Lr0_vars[i].trace(
                                "w", lambda name, index, mode: self.change_and_show_initial())
                            self.Lr0_labels[i].grid(
                                row=i, column=0, sticky=(N, W, E, S))
                            self.Lr0_entries[i].grid(
                                row=i, column=1, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_xl0(self):
        try:
            if self.L0_var.get() and int(self.L0_var.get()) > 0:
                old_count = len(self.xl0_vars)
                for i in range(max(old_count, int(self.L0_var.get() or 0))):
                    if i >= min(old_count, int(self.L0_var.get() or 0)):
                        if old_count > int(self.L0_var.get() or 0):
                            self.xl0_vars = self.xl0_vars[0:i]

                            for ii in range(i, old_count):
                                self.xl0_labels[ii].destroy()
                                self.xl0_entries[ii].destroy()

                            self.xl0_labels = self.xl0_labels[0:i]
                            self.xl0_entries = self.xl0_entries[0:i]
                            break
                        else:
                            self.xl0_vars.append(StringVar())

                            self.xl0_labels.append(
                                ttk.Label(self.xl0_xl0_frame, text=f"x{i + 1}0", style="WhiteBg.TLabel"))
                            self.xl0_entries.append(
                                ttk.Entry(self.xl0_xl0_frame, width=ENTRY_WIDTH, textvariable=self.xl0_vars[i]))

                            self.xl0_vars[i].set("1")
                            self.xl0_vars[i].trace(
                                "w", lambda name, index, mode: self.change_and_show_initial())
                            self.xl0_labels[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))
                            self.xl0_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_yrl0(self):
        try:
            if (self.L0_var.get() and int(self.L0_var.get()) > 0) and (
                    self.R0_var.get() and int(self.R0_var.get()) > 0) \
                    and all([el.get() for el in self.Lr0_vars]) \
                    and all([el.get() for el in self.xl0_vars]):

                old_R0 = len(self.yrl0_vars)
                old_L0 = len(self.yrl0_vars[0])

                for i in range(max(old_R0, int(self.R0_var.get() or 0))):
                    if i >= min(old_R0, int(self.R0_var.get() or 0)):
                        if old_R0 > int(self.R0_var.get() or 0):
                            self.yrl0_vars = self.yrl0_vars[0:i]

                            for ii in range(i, old_R0):
                                for k in range(int(self.L0_var.get() or 0)):
                                    self.yrl0_labels[ii][k].destroy()
                                    self.yrl0_entries[ii][k].destroy()

                            self.yrl0_labels = self.yrl0_labels[0:i]
                            self.yrl0_entries = self.yrl0_entries[0:i]
                            break
                        else:
                            self.yrl0_vars.append(
                                [StringVar() for _ in range(int(self.L0_var.get() or 0))])

                            self.yrl0_labels.append([
                                ttk.Label(self.yrl0_yrl0_frame,
                                          text=f"L{i + 1}0y(x,t)|(x={self.xl0_vars[k].get()},t=0) "
                                               f"= Y{i + 1}{k + 1}0 =", style="WhiteBg.TLabel") for k in
                                range(int(self.L0_var.get() or 0))])
                            self.yrl0_entries.append([
                                ttk.Entry(self.yrl0_yrl0_frame, width=ENTRY_WIDTH,
                                          textvariable=self.yrl0_vars[i][k], state="readonly") for k in
                                range(int(self.L0_var.get() or 0))])

                            for k in range(int(self.L0_var.get() or 0)):
                                self.yrl0_vars[i][k].set(f'phi{i + 1}{k + 1}')
                                self.yrl0_labels[i][k].grid(
                                    row=i, column=k * 2, sticky=(N, W, E, S))
                                self.yrl0_entries[i][k].grid(
                                    row=i, column=k * 2 + 1, sticky=(N, W, E, S))

                    for j in range(max(old_L0, int(self.L0_var.get() or 0))):
                        if j >= min(old_L0, int(self.L0_var.get() or 0)):
                            if old_L0 > int(self.L0_var.get() or 0):
                                self.yrl0_vars[i] = self.yrl0_vars[i][0:j]
                                for k in range(j, old_L0):
                                    self.yrl0_labels[i][k].destroy()
                                    self.yrl0_entries[i][k].destroy()
                                self.yrl0_labels[i] = self.yrl0_labels[i][0:j]
                                self.yrl0_entries[i] = self.yrl0_entries[i][0:j]
                                break
                            else:
                                self.yrl0_vars[i].append(StringVar())
                                self.yrl0_vars[i][j].set(f'phi{i + 1}{j + 1}')

                                self.yrl0_labels[i].append(
                                    ttk.Label(self.yrl0_yrl0_frame,
                                              text=f"L{i + 1}0y(x,t)|(x={self.xl0_vars[j].get()},t=0) "
                                                   f"= Y{i + 1}{j + 1}0 =", style="WhiteBg.TLabel"))
                                self.yrl0_labels[i][j].grid(
                                    row=i, column=j * 2, sticky=(N, W, E, S))

                                self.yrl0_entries[i].append(
                                    ttk.Entry(self.yrl0_yrl0_frame, width=ENTRY_WIDTH,
                                              textvariable=self.yrl0_vars[i][j], state="readonly"))
                                self.yrl0_entries[i][j].grid(
                                    row=i, column=j * 2 + 1, sticky=(N, W, E, S))
                        else:
                            self.yrl0_labels[i][j].destroy()
                            self.yrl0_labels[i][j] = ttk.Label(self.yrl0_yrl0_frame,
                                                               text=f"L{i + 1}0y(x,t)|(x={self.xl0_vars[j].get()},t=0) "
                                                                    f"= Y{i + 1}{j + 1}0 =", style="WhiteBg.TLabel")
                            self.yrl0_labels[i][j].grid(
                                row=i, column=j * 2, sticky=(N, W, E, S))

        except Exception as e:
            raise e

    def change_and_show_initial(self):
        try:
            self.change_and_show_Lr0()
            self.change_and_show_xl0()
            self.change_and_show_yrl0()
        except Exception as e:
            raise e
