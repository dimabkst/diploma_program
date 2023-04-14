from tkinter import *
from tkinter import ttk

ENTRY_WIDTH = 10

class v_input:

    def __init__(self, root):

        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
        s.configure("VectorWhiteBg.TFrame", background="white", borderwidth=5, relief="solid")
        s.configure("WhiteBg.TFrame", background="white")
        s.configure("WhiteBg.TLabel", background="white")

        # Frames
        self.root = ttk.Frame(root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.root.grid(column=0, row=0, sticky=(N, W, E, S))

        self.count_frame = ttk.Frame(self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.count_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.v_frame = ttk.Frame(self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.v_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        #

        # Count input
        self.count_label_frame = ttk.Frame(self.count_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.count_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.count_entry_frame = ttk.Frame(self.count_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.count_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.count_var = StringVar()
        self.count_var.set("1")
        self.count_var.trace("w", lambda name, index, mode: self.change_and_show_v())

        ttk.Label(self.count_label_frame, text="Кількість векторів v(x,t) -", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))

        self.count_entry = ttk.Entry(self.count_entry_frame, width=ENTRY_WIDTH, textvariable=self.count_var)
        self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
        #

        # v input
        self.v_label_frame = ttk.Frame(self.v_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.v_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.v_v_frame = ttk.Frame(self.v_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.v_v_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.v0_vars = []
        self.v0_entries = []
        self.vG_vars = []
        self.vG_entries = []

        for i in range(int(self.count_var.get() or 0)):
            self.v0_vars.append(StringVar())
            self.v0_vars[i].set("0")
            self.vG_vars.append(StringVar())
            self.vG_vars[i].set("0")

            self.v0_entries.append(ttk.Entry(self.v_v_frame, width=ENTRY_WIDTH, textvariable=self.v0_vars[i]))
            self.v0_entries[i].grid(row=0, column=i, sticky=(N, W, E, S))

            self.vG_entries.append(ttk.Entry(self.v_v_frame, width=ENTRY_WIDTH, textvariable=self.vG_vars[i]))
            self.vG_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))

        ttk.Label(self.v_label_frame, text="Вектори v(x,t):", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))
        #

        # Align
        self.align_rows_cols(self.count_label_frame)
        self.align_rows_cols(self.count_entry_frame)
        self.align_rows_cols(self.count_frame)

        self.align_rows_cols(self.v_label_frame)
        self.align_rows_cols(self.v_v_frame)
        self.align_rows_cols(self.v_frame)

        self.align_rows_cols(self.root)
        #

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)

    def change_and_show_v(self):
        try:
            if self.count_var.get() and int(self.count_var.get()) > 0:
                old_count = len(self.v0_vars)
                for i in range(max(old_count, int(self.count_var.get() or 0))):
                    if i >= min(old_count, int(self.count_var.get() or 0)):
                        if old_count > int(self.count_var.get() or 0):
                            self.v0_vars = self.v0_vars[0:i]
                            self.vG_vars = self.vG_vars[0:i]

                            for ii in range(i, old_count):
                                self.v0_entries[ii].destroy()
                                self.vG_entries[ii].destroy()

                            self.v0_entries = self.v0_entries[0:i]
                            self.vG_entries = self.vG_entries[0:i]
                            break
                        else:
                            self.v0_vars.append(StringVar())
                            self.vG_vars.append(StringVar())

                            self.v0_entries.append(
                                ttk.Entry(self.v_v_frame, width=ENTRY_WIDTH,
                                          textvariable=self.v0_vars[i]))
                            self.vG_entries.append(
                                ttk.Entry(self.v_v_frame, width=ENTRY_WIDTH,
                                          textvariable=self.vG_vars[i]))

                            self.v0_vars[i].set("0")
                            self.v0_entries[i].grid(row=0, column=i, sticky=(N, W, E, S))

                            self.vG_vars[i].set("0")
                            self.vG_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e
