from tkinter import *
from tkinter import ttk
from view.utils import align_rows_cols

ENTRY_WIDTH = 10


class boundary_conditions_input:

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

            self.boundary_frame = ttk.Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.boundary_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            #

            # boundary conditions
            self.boundary_top_frame = ttk.Frame(
                self.boundary_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.boundary_top_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            self.boundary_bot_frame = ttk.Frame(
                self.boundary_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.boundary_bot_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.boundary_top_left_frame = ttk.Frame(
                self.boundary_top_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.boundary_top_left_frame.grid(
                column=0, row=0, sticky=(N, W, E, S))

            self.boundary_top_right_frame = ttk.Frame(
                self.boundary_top_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.boundary_top_right_frame.grid(
                column=1, row=0, sticky=(N, W, E, S))

            # RG input
            self.RG_frame = ttk.Frame(
                self.boundary_top_left_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.RG_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.RG_label_frame = ttk.Frame(
                self.RG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.RG_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.RG_entry_frame = ttk.Frame(
                self.RG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.RG_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.RG_var = StringVar()
            self.RG_var.set("1")
            self.RG_var.trace("w", lambda name, index,
                              mode: self.change_and_show_boundary())

            ttk.Label(self.RG_label_frame, text="Кількість крайових операторів LrG(dx) RG -", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = ttk.Entry(
                self.RG_entry_frame, width=ENTRY_WIDTH, textvariable=self.RG_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # LrG input
            self.LrG_frame = ttk.Frame(
                self.boundary_top_left_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.LrG_frame.grid(column=0, row=1, sticky=(N, W, E, S))
            self.LrG_label_frame = ttk.Frame(
                self.LrG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.LrG_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.LrG_LrG_frame = ttk.Frame(
                self.LrG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.LrG_LrG_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.LrG_labels = []
            self.LrG_vars = []
            self.LrG_entries = []

            for i in range(int(self.RG_var.get() or 0)):
                self.LrG_vars.append(StringVar())
                self.LrG_vars[i].set("1*d[x,0]")
                self.LrG_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_boundary())

                self.LrG_labels.append(
                    ttk.Label(self.LrG_LrG_frame, text=f"L{i + 1}G(dx):", style="WhiteBg.TLabel"))
                self.LrG_labels[i].grid(row=i, column=0, sticky=(N, W, E, S))

                self.LrG_entries.append(ttk.Entry(
                    self.LrG_LrG_frame, width=ENTRY_WIDTH, textvariable=self.LrG_vars[i]))
                self.LrG_entries[i].grid(row=i, column=1, sticky=(N, W, E, S))

            ttk.Label(self.LrG_label_frame, text="Крайові оператори LrG(dx):", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # LG input
            self.LG_frame = ttk.Frame(
                self.boundary_top_right_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.LG_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.LG_label_frame = ttk.Frame(
                self.LG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.LG_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.LG_entry_frame = ttk.Frame(
                self.LG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.LG_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.LG_var = StringVar()
            self.LG_var.set("1")
            self.LG_var.trace("w", lambda name, index,
                              mode: self.change_and_show_boundary())

            ttk.Label(self.LG_label_frame, text="Кількість дискретних точок спостережень LrG(dx) LG -",
                      style="WhiteBg.TLabel").grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = ttk.Entry(
                self.LG_entry_frame, width=ENTRY_WIDTH, textvariable=self.LG_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # slG input
            self.slG_frame = ttk.Frame(
                self.boundary_top_right_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.slG_frame.grid(column=0, row=1, sticky=(N, W, E, S))
            self.slG_label_frame = ttk.Frame(
                self.slG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.slG_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.slG_slG_frame = ttk.Frame(
                self.slG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.slG_slG_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            self.slG_labels = []
            self.slG_vars = []
            self.slG_entries = []

            for i in range(int(self.LG_var.get() or 0)):
                self.slG_vars.append(StringVar())
                self.slG_vars[i].set("(0,0)")
                self.slG_vars[i].trace(
                    "w", lambda name, index, mode: self.change_and_show_boundary())

                self.slG_labels.append(
                    ttk.Label(self.slG_slG_frame, text=f"s{i + 1}G", style="WhiteBg.TLabel"))
                self.slG_labels[i].grid(row=0, column=i, sticky=(N, W, E, S))

                self.slG_entries.append(ttk.Entry(
                    self.slG_slG_frame, width=ENTRY_WIDTH, textvariable=self.slG_vars[i]))
                self.slG_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))

            ttk.Label(self.slG_label_frame, text="Дискретні точки спостережень LrG(dx), slG є SG x [0, T] у форматі:",
                      style="WhiteBg.TLabel").grid(column=0, row=0, sticky=(N, E, W, S))
            slG_format_image = PhotoImage(file="./assets/slG.gif")
            slG_format_image_label = ttk.Label(
                self.slG_label_frame, image=slG_format_image, style="WhiteBg.TLabel")
            slG_format_image_label.image = slG_format_image
            slG_format_image_label.grid(column=1, row=0, sticky=(N, E, W, S))
            #

            # YrlG input
            self.yrlG_frame = ttk.Frame(
                self.boundary_bot_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yrlG_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.yrlG_label_frame = ttk.Frame(
                self.yrlG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yrlG_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.yrlG_yrlG_frame = ttk.Frame(
                self.yrlG_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.yrlG_yrlG_frame.grid(column=0, row=1, sticky=(N, W, E, S))

            ttk.Label(self.yrlG_label_frame, text="Крайові спостереження YrlG процесу:", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.yrlG_labels = []
            self.yrlG_vars = []
            self.yrlG_entries = []

            for r in range(int(self.RG_var.get() or 0)):
                self.yrlG_labels.append([])
                self.yrlG_vars.append([])
                self.yrlG_entries.append([])

                for l in range(int(self.LG_var.get() or 0)):
                    self.yrlG_labels[r].append(ttk.Label(self.yrlG_yrlG_frame,
                                                         text=f"L{r + 1}Gy(x,t)|(x,t)={self.slG_vars[l].get()} "
                                                         f"= Y{r + 1}{l + 1}G =", style="WhiteBg.TLabel"))
                    self.yrlG_labels[r][l].grid(
                        row=r, column=l * 2, sticky=(N, W, E, S))

                    self.yrlG_vars[r].append(StringVar())
                    self.yrlG_vars[r][l].set("0")
                    self.yrlG_vars[r][l].trace(
                        "w", lambda name, index, mode: self.change_and_show_boundary())

                    self.yrlG_entries[r].append(ttk.Entry(self.yrlG_yrlG_frame, width=ENTRY_WIDTH,
                                                          textvariable=self.yrlG_vars[r][l]))
                    self.yrlG_entries[r][l].grid(
                        row=r, column=l * 2 + 1, sticky=(N, W, E, S))
            #

            # Align everything
            align_rows_cols(self.RG_label_frame)
            align_rows_cols(self.RG_entry_frame)
            align_rows_cols(self.RG_frame)

            align_rows_cols(self.LrG_frame)
            align_rows_cols(self.LrG_label_frame)
            align_rows_cols(self.LrG_LrG_frame)

            align_rows_cols(self.LG_label_frame)
            align_rows_cols(self.LG_entry_frame)
            align_rows_cols(self.LG_frame)

            align_rows_cols(self.slG_frame)
            align_rows_cols(self.slG_label_frame)
            align_rows_cols(self.slG_slG_frame)

            align_rows_cols(self.boundary_top_left_frame)
            align_rows_cols(self.boundary_top_right_frame)
            align_rows_cols(self.boundary_top_frame)

            align_rows_cols(self.yrlG_frame)
            align_rows_cols(self.yrlG_label_frame)
            align_rows_cols(self.yrlG_yrlG_frame)

            align_rows_cols(self.boundary_bot_frame)

            align_rows_cols(self.boundary_frame)

            align_rows_cols(self.root)
            #
        except Exception as e:
            raise e

    def change_and_show_LrG(self):
        try:
            if self.RG_var.get() and int(self.RG_var.get()) > 0:
                old_count = len(self.LrG_vars)
                for i in range(max(old_count, int(self.RG_var.get() or 0))):
                    if i >= min(old_count, int(self.RG_var.get() or 0)):
                        if old_count > int(self.RG_var.get() or 0):
                            self.LrG_vars = self.LrG_vars[0:i]

                            for ii in range(i, old_count):
                                self.LrG_labels[ii].destroy()
                                self.LrG_entries[ii].destroy()

                            self.LrG_labels = self.LrG_labels[0:i]
                            self.LrG_entries = self.LrG_entries[0:i]
                            break
                        else:
                            self.LrG_vars.append(StringVar())

                            self.LrG_labels.append(
                                ttk.Label(self.LrG_LrG_frame, text=f"L{i + 1}G(dx):", style="WhiteBg.TLabel"))
                            self.LrG_entries.append(
                                ttk.Entry(self.LrG_LrG_frame, width=ENTRY_WIDTH,
                                          textvariable=self.LrG_vars[i]))

                            self.LrG_vars[i].set("1*d[x,0]")
                            self.LrG_vars[i].trace(
                                "w", lambda name, index, mode: self.change_and_show_boundary())
                            self.LrG_labels[i].grid(
                                row=i, column=0, sticky=(N, W, E, S))
                            self.LrG_entries[i].grid(
                                row=i, column=1, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_slG(self):
        try:
            if self.LG_var.get() and int(self.LG_var.get()) > 0:
                old_count = len(self.slG_vars)
                for i in range(max(old_count, int(self.LG_var.get() or 0))):
                    if i >= min(old_count, int(self.LG_var.get() or 0)):
                        if old_count > int(self.LG_var.get() or 0):
                            self.slG_vars = self.slG_vars[0:i]

                            for ii in range(i, old_count):
                                self.slG_labels[ii].destroy()
                                self.slG_entries[ii].destroy()

                            self.slG_labels = self.slG_labels[0:i]
                            self.slG_entries = self.slG_entries[0:i]
                            break
                        else:
                            self.slG_vars.append(StringVar())

                            self.slG_labels.append(
                                ttk.Label(self.slG_slG_frame, text=f"s{i + 1}G", style="WhiteBg.TLabel"))
                            self.slG_entries.append(
                                ttk.Entry(self.slG_slG_frame, width=ENTRY_WIDTH, textvariable=self.slG_vars[i]))

                            self.slG_vars[i].set("(0,0)")
                            self.slG_vars[i].trace(
                                "w", lambda name, index, mode: self.change_and_show_boundary())
                            self.slG_labels[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))
                            self.slG_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e

    def change_and_show_yrlG(self):
        try:
            if (self.LG_var.get() and int(self.LG_var.get()) > 0) and (
                    self.RG_var.get() and int(self.RG_var.get()) > 0) \
                    and all([el.get() for el in self.LrG_vars])\
                    and all([el.get() for el in self.slG_vars]):

                old_RG = len(self.yrlG_vars)
                old_LG = len(self.yrlG_vars[0])

                for i in range(max(old_RG, int(self.RG_var.get() or 0))):
                    if i >= min(old_RG, int(self.RG_var.get() or 0)):
                        if old_RG > int(self.RG_var.get() or 0):
                            self.yrlG_vars = self.yrlG_vars[0:i]

                            for ii in range(i, old_RG):
                                for k in range(int(self.LG_var.get() or 0)):
                                    self.yrlG_labels[ii][k].destroy()
                                    self.yrlG_entries[ii][k].destroy()

                            self.yrlG_labels = self.yrlG_labels[0:i]
                            self.yrlG_entries = self.yrlG_entries[0:i]
                            break
                        else:
                            self.yrlG_vars.append(
                                [StringVar() for _ in range(int(self.LG_var.get() or 0))])

                            self.yrlG_labels.append([
                                ttk.Label(self.yrlG_yrlG_frame,
                                          text=f"L{i + 1}Gy(x,t)|(x,t)={self.slG_vars[k].get()} "
                                               f"= Y{i + 1}{k + 1}G =", style="WhiteBg.TLabel") for k in
                                range(int(self.LG_var.get() or 0))])
                            self.yrlG_entries.append([
                                ttk.Entry(self.yrlG_yrlG_frame, width=ENTRY_WIDTH,
                                          textvariable=self.yrlG_vars[i][k]) for k in
                                range(int(self.LG_var.get() or 0))])

                            for k in range(int(self.LG_var.get() or 0)):
                                self.yrlG_vars[i][k].set("0")
                                self.yrlG_labels[i][k].grid(
                                    row=i, column=k * 2, sticky=(N, W, E, S))
                                self.yrlG_entries[i][k].grid(
                                    row=i, column=k * 2 + 1, sticky=(N, W, E, S))

                    for j in range(max(old_LG, int(self.LG_var.get() or 0))):
                        if j >= min(old_LG, int(self.LG_var.get() or 0)):
                            if old_LG > int(self.LG_var.get() or 0):
                                self.yrlG_vars[i] = self.yrlG_vars[i][0:j]
                                for k in range(j, old_LG):
                                    self.yrlG_labels[i][k].destroy()
                                    self.yrlG_entries[i][k].destroy()
                                self.yrlG_labels[i] = self.yrlG_labels[i][0:j]
                                self.yrlG_entries[i] = self.yrlG_entries[i][0:j]
                                break
                            else:
                                self.yrlG_vars[i].append(StringVar())
                                self.yrlG_vars[i][j].set("0")

                                self.yrlG_labels[i].append(
                                    ttk.Label(self.yrlG_yrlG_frame,
                                              text=f"L{i + 1}Gy(x,t)|(x,t)={self.slG_vars[j].get()} "
                                                   f"= Y{i + 1}{j + 1}G =", style="WhiteBg.TLabel"))
                                self.yrlG_labels[i][j].grid(
                                    row=i, column=j * 2, sticky=(N, W, E, S))

                                self.yrlG_entries[i].append(
                                    ttk.Entry(self.yrlG_yrlG_frame, width=ENTRY_WIDTH,
                                              textvariable=self.yrlG_vars[i][j]))
                                self.yrlG_entries[i][j].grid(
                                    row=i, column=j * 2 + 1, sticky=(N, W, E, S))
                        else:
                            self.yrlG_labels[i][j].destroy()
                            self.yrlG_labels[i][j] = ttk.Label(self.yrlG_yrlG_frame,
                                                               text=f"L{i + 1}Gy(x,t)|(x,t)={self.slG_vars[j].get()} "
                                                                    f"= Y{i + 1}{j + 1}G =", style="WhiteBg.TLabel")
                            self.yrlG_labels[i][j].grid(
                                row=i, column=j * 2, sticky=(N, W, E, S))

        except Exception as e:
            raise e

    def change_and_show_boundary(self):
        try:
            self.change_and_show_LrG()
            self.change_and_show_slG()
            self.change_and_show_yrlG()
        except Exception as e:
            raise e
