from tkinter import N, E, W, S, StringVar
from tkinter.ttk import Label, Entry
from view.utils import ENTRY_WIDTH,  create_grid_frame, create_frame_label_entrie_frames


class v_input:

    def __init__(self, root):
        try:
            self.root = create_grid_frame(
                root=root, column=0, row=0, style="TopWhiteBg.TFrame")

            # Count input
            self.count_frame, self.count_label_frame, self.count_entry_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=0, isRow=True, style="TopWhiteBg.TFrame")

            self.count_var = StringVar()
            self.count_var.set("1")
            self.count_var.trace("w", lambda name, index,
                                 mode: self.change_and_show_v())

            Label(self.count_label_frame, text="Кількість векторів v(x,t) -", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.count_entry = Entry(
                self.count_entry_frame, width=ENTRY_WIDTH, textvariable=self.count_var)
            self.count_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # v input
            self.v_frame, self.v_label_frame, self.v_v_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=1, isRow=True, style="TopWhiteBg.TFrame")

            self.v0_vars = []
            self.v0_entries = []
            self.vG_vars = []
            self.vG_entries = []

            for i in range(int(self.count_var.get() or 0)):
                self.v0_vars.append(StringVar())
                self.v0_vars[i].set("0")
                self.vG_vars.append(StringVar())
                self.vG_vars[i].set("0")

                self.v0_entries.append(
                    Entry(self.v_v_frame, width=ENTRY_WIDTH, textvariable=self.v0_vars[i]))
                self.v0_entries[i].grid(row=0, column=i, sticky=(N, W, E, S))

                self.vG_entries.append(
                    Entry(self.v_v_frame, width=ENTRY_WIDTH, textvariable=self.vG_vars[i]))
                self.vG_entries[i].grid(row=1, column=i, sticky=(N, W, E, S))

            Label(self.v_label_frame, text="Вектори v(x,t):", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
            #
        except Exception as e:
            raise e

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
                                Entry(self.v_v_frame, width=ENTRY_WIDTH,
                                      textvariable=self.v0_vars[i]))
                            self.vG_entries.append(
                                Entry(self.v_v_frame, width=ENTRY_WIDTH,
                                      textvariable=self.vG_vars[i]))

                            self.v0_vars[i].set("0")
                            self.v0_entries[i].grid(
                                row=0, column=i, sticky=(N, W, E, S))

                            self.vG_vars[i].set("0")
                            self.vG_entries[i].grid(
                                row=1, column=i, sticky=(N, W, E, S))
        except Exception as e:
            raise e
