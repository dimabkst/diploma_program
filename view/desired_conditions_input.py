from tkinter import *
from tkinter import ttk

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
            self.align_rows_cols(self.I_label_frame)
            self.align_rows_cols(self.I_entry_frame)
            self.align_rows_cols(self.I_frame)

            self.align_rows_cols(self.Li_frame)
            self.align_rows_cols(self.Li_label_frame)
            self.align_rows_cols(self.Li_Li_frame)

            self.align_rows_cols(self.Ji_label_frame)
            self.align_rows_cols(self.Ji_Ji_frame)
            self.align_rows_cols(self.Ji_frame)

            self.align_rows_cols(self.sij_frame)
            self.align_rows_cols(self.sij_label_frame)
            self.align_rows_cols(self.sij_sij_frame)

            self.align_rows_cols(self.desired_top_left_frame)
            self.align_rows_cols(self.desired_top_right_frame)
            self.align_rows_cols(self.desired_top_frame)

            self.align_rows_cols(self.yij_frame)
            self.align_rows_cols(self.yij_label_frame)
            self.align_rows_cols(self.yij_yij_frame)

            self.align_rows_cols(self.desired_bot_frame)

            self.align_rows_cols(self.desired_frame)

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

    def change_and_show_Li(self):
        try:
            if self.I_var.get() and int(self.I_var.get()) > 0:
                old_count = len(self.Li_vars)
                for i in range(max(old_count, int(self.I_var.get() or 0))):
                    if i >= min(old_count, int(self.I_var.get() or 0)):
                        if old_count > int(self.I_var.get() or 0):
                            self.Li_vars = self.Li_vars[0:i]

                            for ii in range(i, old_count):
                                self.Li_labels[ii].destroy()
                                self.Li_entries[ii].destroy()

                            self.Li_labels = self.Li_labels[0:i]
                            self.Li_entries = self.Li_entries[0:i]
                            break
                        else:
                            self.Li_vars.append(StringVar())

                            self.Li_labels.append(
                                ttk.Label(self.Li_Li_frame, text=f"L{i + 1}(dx, dt):", style="WhiteBg.TLabel"))
                            self.Li_entries.append(
                                ttk.Entry(self.Li_Li_frame, width=ENTRY_WIDTH,
                                          textvariable=self.Li_vars[i]))

                            self.Li_vars[i].set("1*d[x,0]")
                            self.Li_vars[i].trace(
                                "w", lambda name, index, mode: self.change_and_show_desired())
                            self.Li_labels[i].grid(
                                row=i, column=0, sticky=(N, W, E, S))
                            self.Li_entries[i].grid(
                                row=i, column=1, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_Ji(self):
        try:
            if self.I_var.get() and int(self.I_var.get()) > 0:
                old_count = len(self.Ji_vars)
                for i in range(max(old_count, int(self.I_var.get() or 0))):
                    if i >= min(old_count, int(self.I_var.get() or 0)):
                        if old_count > int(self.I_var.get() or 0):
                            self.Ji_vars = self.Ji_vars[0:i]

                            for ii in range(i, old_count):
                                self.Ji_labels[ii].destroy()
                                self.Ji_entries[ii].destroy()

                            self.Ji_labels = self.Ji_labels[0:i]
                            self.Ji_entries = self.Ji_entries[0:i]
                            break
                        else:
                            self.Ji_vars.append(StringVar())

                            self.Ji_labels.append(ttk.Label(self.Ji_Ji_frame, text=f"J{i+1}",
                                                            style="WhiteBg.TLabel"))
                            self.Ji_entries.append(
                                ttk.Entry(self.Ji_Ji_frame, width=ENTRY_WIDTH, textvariable=self.Ji_vars[i]))

                            self.Ji_vars[i].set("1")
                            self.Ji_vars[i].trace(
                                "w", lambda name, index, mode: self.change_and_show_desired())
                            self.Ji_labels[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))
                            self.Ji_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_sij(self):
        try:
            if (self.I_var.get() and int(self.I_var.get()) > 0)\
                and all([el.get() and int(el.get()) > 0 for el in self.Ji_vars]) \
                    and all([el.get() for el in self.Li_vars]):

                old_I = len(self.sij_vars)

                for i in range(max(old_I, int(self.I_var.get() or 0))):
                    try:
                        old_Ji = len(self.sij_vars[i])
                    except IndexError:
                        old_Ji = 0

                    if i >= min(old_I, int(self.I_var.get() or 0)):
                        if old_I > int(self.I_var.get() or 0):
                            self.sij_vars = self.sij_vars[0:i]

                            for ii in range(i, old_I):
                                for k in range(old_Ji):
                                    self.sij_labels[ii][k].destroy()
                                    self.sij_entries[ii][k].destroy()

                            self.sij_labels = self.sij_labels[0:i]
                            self.sij_entries = self.sij_entries[0:i]
                            break
                        else:
                            self.sij_vars.append(
                                [StringVar() for _ in range(int(self.Ji_vars[i].get() or 0))])

                            self.sij_labels.append([
                                ttk.Label(self.sij_sij_frame, text=f"s{i + 1}{k + 1}", style="WhiteBg.TLabel") for k in
                                range(int(self.Ji_vars[i].get() or 0))])
                            self.sij_entries.append([
                                ttk.Entry(self.sij_sij_frame, width=ENTRY_WIDTH,
                                          textvariable=self.sij_vars[i][k]) for k in
                                range(int(self.Ji_vars[i].get() or 0))])

                            for k in range(int(self.Ji_vars[i].get() or 0)):
                                self.sij_vars[i][k].set("(0,0)")
                                self.sij_vars[i][k].trace(
                                    "w", lambda name, index, mode: self.change_and_show_desired())
                                self.sij_labels[i][k].grid(
                                    row=i, column=k * 2, sticky=(N, W, E, S))
                                self.sij_entries[i][k].grid(
                                    row=i, column=k * 2 + 1, sticky=(N, W, E, S))

                    try:
                        old_Ji = len(self.sij_vars[i])
                    except IndexError:
                        old_Ji = 0

                    for j in range(max(old_Ji, int(self.Ji_vars[i].get() or 0))):
                        if j >= min(old_Ji, int(self.Ji_vars[i].get() or 0)):
                            if old_Ji > int(self.Ji_vars[i].get() or 0):
                                self.sij_vars[i] = self.sij_vars[i][0:j]
                                for k in range(j, old_Ji):
                                    self.sij_labels[i][k].destroy()
                                    self.sij_entries[i][k].destroy()
                                self.sij_labels[i] = self.sij_labels[i][0:j]
                                self.sij_entries[i] = self.sij_entries[i][0:j]
                                break
                            else:
                                self.sij_vars[i].append(StringVar())
                                self.sij_vars[i][j].set("(0,0)")
                                self.sij_vars[i][j].trace(
                                    "w", lambda name, index, mode: self.change_and_show_desired())

                                self.sij_labels[i].append(
                                    ttk.Label(self.sij_sij_frame, text=f"s{i + 1}{j + 1}", style="WhiteBg.TLabel"))
                                self.sij_labels[i][j].grid(
                                    row=i, column=j * 2, sticky=(N, W, E, S))

                                self.sij_entries[i].append(
                                    ttk.Entry(self.sij_sij_frame, width=ENTRY_WIDTH,
                                              textvariable=self.sij_vars[i][j]))
                                self.sij_entries[i][j].grid(
                                    row=i, column=j * 2 + 1, sticky=(N, W, E, S))
                        else:
                            self.sij_labels[i][j].destroy()
                            self.sij_labels[i][j] = ttk.Label(
                                self.sij_sij_frame, text=f"s{i + 1}{j + 1}", style="WhiteBg.TLabel")
                            self.sij_labels[i][j].grid(
                                row=i, column=j * 2, sticky=(N, W, E, S))

        except Exception as e:
            raise e

    def change_and_show_yij(self):
        try:
            if (self.I_var.get() and int(self.I_var.get()) > 0)\
                    and all([el.get() and int(el.get()) > 0 for el in self.Ji_vars]) \
                and all([el.get() for el in self.Li_vars]) \
                    and all([all([el.get() for el in row]) for row in self.sij_vars]):

                old_I = len(self.yij_vars)

                for i in range(max(old_I, int(self.I_var.get() or 0))):
                    try:
                        old_Ji = len(self.yij_vars[i])
                    except IndexError:
                        old_Ji = 0

                    if i >= min(old_I, int(self.I_var.get() or 0)):
                        if old_I > int(self.I_var.get() or 0):
                            self.yij_vars = self.yij_vars[0:i]

                            for ii in range(i, old_I):
                                for k in range(old_Ji):
                                    self.yij_labels[ii][k].destroy()
                                    self.yij_entries[ii][k].destroy()

                            self.yij_labels = self.yij_labels[0:i]
                            self.yij_entries = self.yij_entries[0:i]
                            break
                        else:
                            self.yij_vars.append(
                                [StringVar() for _ in range(int(self.Ji_vars[i].get() or 0))])

                            self.yij_labels.append([
                                ttk.Label(self.yij_yij_frame,
                                          text=f"L{i + 1}y(x,t)|(x,t)={self.sij_vars[i][k].get()} "
                                               f"= Y{i + 1}{k + 1} =", style="WhiteBg.TLabel") for k in
                                range(int(self.Ji_vars[i].get() or 0))])
                            self.yij_entries.append([
                                ttk.Entry(self.yij_yij_frame, width=ENTRY_WIDTH,
                                          textvariable=self.yij_vars[i][k]) for k in
                                range(int(self.Ji_vars[i].get() or 0))])

                            for k in range(int(self.Ji_vars[i].get() or 0)):
                                self.yij_vars[i][k].set("0")
                                # self.yij_vars[i][k].trace("w", lambda name, index, mode: self.change_and_show_desired())
                                self.yij_labels[i][k].grid(
                                    row=i, column=k * 2, sticky=(N, W, E, S))
                                self.yij_entries[i][k].grid(
                                    row=i, column=k * 2 + 1, sticky=(N, W, E, S))

                    try:
                        old_Ji = len(self.yij_vars[i])
                    except IndexError:
                        old_Ji = 0

                    for j in range(max(old_Ji, int(self.Ji_vars[i].get() or 0))):
                        if j >= min(old_Ji, int(self.Ji_vars[i].get() or 0)):
                            if old_Ji > int(self.Ji_vars[i].get() or 0):
                                self.yij_vars[i] = self.yij_vars[i][0:j]
                                for k in range(j, old_Ji):
                                    self.yij_labels[i][k].destroy()
                                    self.yij_entries[i][k].destroy()
                                self.yij_labels[i] = self.yij_labels[i][0:j]
                                self.yij_entries[i] = self.yij_entries[i][0:j]
                                break
                            else:
                                self.yij_vars[i].append(StringVar())
                                self.yij_vars[i][j].set("0")
                                # self.yij_vars[i][j].trace("w", lambda name, index, mode: self.change_and_show_desired())

                                self.yij_labels[i].append(
                                    ttk.Label(self.yij_yij_frame,
                                              text=f"L{i + 1}y(x,t)|(x,t)={self.sij_vars[i][j].get()} "
                                              f"= Y{i + 1}{j + 1} =", style="WhiteBg.TLabel"))
                                self.yij_labels[i][j].grid(
                                    row=i, column=j * 2, sticky=(N, W, E, S))

                                self.yij_entries[i].append(
                                    ttk.Entry(self.yij_yij_frame, width=ENTRY_WIDTH,
                                              textvariable=self.yij_vars[i][j]))
                                self.yij_entries[i][j].grid(
                                    row=i, column=j * 2 + 1, sticky=(N, W, E, S))
                        else:
                            self.yij_labels[i][j].destroy()
                            self.yij_labels[i][j] = ttk.Label(self.yij_yij_frame,
                                                              text=f"L{i + 1}y(x,t)|(x,t)={self.sij_vars[i][j].get()} "
                                                              f"= Y{i + 1}{j + 1} =", style="WhiteBg.TLabel")
                            self.yij_labels[i][j].grid(
                                row=i, column=j * 2, sticky=(N, W, E, S))

        except Exception as e:
            raise e

    def change_and_show_desired(self):
        try:
            self.change_and_show_Li()
            self.change_and_show_Ji()
            self.change_and_show_sij()
            self.change_and_show_yij()
        except Exception as e:
            raise e
