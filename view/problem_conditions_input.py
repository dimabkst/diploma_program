from tkinter import N, E, W, S, StringVar, Scrollbar, HORIZONTAL, PhotoImage
from tkinter.ttk import Frame, Label, Entry
from view.utils import ENTRY_WIDTH, align_rows_cols, create_frame_label_entrie_frames


class problem_conditions_input:

    def __init__(self, root):
        try:
            self.root = Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            # S_input
            self.S_frame, self.S_label_frame, self.S_entry_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=0, isRow=True, style="TopWhiteBg.TFrame")

            self.S_var = StringVar()
            self.S_var.set("[0, 1]")

            Label(self.S_label_frame, text="S =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.S_entry = Entry(
                self.S_entry_frame, width=ENTRY_WIDTH, textvariable=self.S_var)
            self.S_entry_hsb = Scrollbar(
                self.S_entry_frame, orient=HORIZONTAL, command=self.S_entry.xview)
            self.S_entry.configure(xscrollcommand=self.S_entry_hsb.set)
            self.S_entry_hsb.grid(column=0, row=1, sticky=(E, W))
            self.S_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # S0_input
            self.S0_frame, self.S0_label_frame, self.S0_entry_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=1, isRow=True, style="TopWhiteBg.TFrame")

            self.S0_label_frame = Frame(
                self.S0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.S0_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
            self.S0_entry_frame = Frame(
                self.S0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.S0_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

            self.S0_var = StringVar()
            self.S0_var.set("[0, 1]")

            Label(self.S0_label_frame, text="S0 =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.S0_entry = Entry(
                self.S0_entry_frame, width=ENTRY_WIDTH, textvariable=self.S0_var)
            self.S0_entry_hsb = Scrollbar(
                self.S0_entry_frame, orient=HORIZONTAL, command=self.S0_entry.xview)
            self.S0_entry.configure(xscrollcommand=self.S0_entry_hsb.set)
            self.S0_entry_hsb.grid(column=0, row=1, sticky=(E, W))
            self.S0_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # SG_input
            self.SG_frame, self.SG_label_frame, self.SG_entry_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=2, isRow=True, style="TopWhiteBg.TFrame")

            self.SG_var = StringVar()
            self.SG_var.set("[0, 1]")

            Label(self.SG_label_frame, text="SG =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.SG_entry = Entry(
                self.SG_entry_frame, width=ENTRY_WIDTH, textvariable=self.SG_var)
            self.SG_entry_hsb = Scrollbar(
                self.SG_entry_frame, orient=HORIZONTAL, command=self.SG_entry.xview)
            self.SG_entry.configure(xscrollcommand=self.SG_entry_hsb.set)
            self.SG_entry_hsb.grid(column=0, row=1, sticky=(E, W))
            self.SG_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # T_input
            self.T_frame, self.T_label_frame, self.T_entry_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=3, isRow=True, style="TopWhiteBg.TFrame")

            self.T_var = StringVar()
            self.T_var.set("5")

            Label(self.T_label_frame, text="T =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.T_entry = Entry(
                self.T_entry_frame, width=ENTRY_WIDTH, textvariable=self.T_var)
            self.T_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # L_input
            self.L_frame, self.L_label_frame, self.L_entry_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=4, isRow=True, style="TopWhiteBg.TFrame")

            self.L_format_frame = Frame(
                self.L_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
            self.L_format_frame.grid(column=1, row=1, sticky=(N, W, E, S))

            self.L_var = StringVar()
            self.L_var.set("1*d[t,1]-1*d[x,2]")

            Label(self.L_label_frame, text="L(dx,dt) =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.L_entry = Entry(
                self.L_entry_frame, width=ENTRY_WIDTH, textvariable=self.L_var)
            self.L_entry.grid(column=0, row=0, sticky=(N, E, W, S))

            Label(self.L_format_frame, text="Формат вводу частинних похідних:", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            L_format_image = PhotoImage(file="./assets/derivative.gif")
            L_format_image_label = Label(
                self.L_format_frame, image=L_format_image, style="WhiteBg.TLabel")
            L_format_image_label.image = L_format_image
            L_format_image_label.grid(column=1, row=0, sticky=(N, E, W, S))
            #

            # u_input
            self.u_frame, self.u_label_frame, self.u_entry_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=5, isRow=True, style="TopWhiteBg.TFrame")

            self.u_var = StringVar()
            self.u_var.set("0")

            Label(self.u_label_frame, text="u(x,t) =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.u_entry = Entry(
                self.u_entry_frame, width=ENTRY_WIDTH, textvariable=self.u_var)
            self.u_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # G_input
            self.G_frame, self.G_label_frame, self.G_entry_frame = create_frame_label_entrie_frames(
                root=self.root, column=0, row=6, isRow=True, style="TopWhiteBg.TFrame")

            self.G_var = StringVar()
            self.G_var.set("Heaviside(t)*exp(-x^2/(4*t)) / sqrt(4 * pi * t)")

            Label(self.G_label_frame, text="G(x,t) =", style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            self.G_entry = Entry(
                self.G_entry_frame, width=ENTRY_WIDTH, textvariable=self.G_var)
            self.G_entry_hsb = Scrollbar(
                self.G_entry_frame, orient=HORIZONTAL, command=self.G_entry.xview)
            self.G_entry.configure(xscrollcommand=self.G_entry_hsb.set)
            self.G_entry_hsb.grid(column=0, row=1, sticky=(E, W))
            self.G_entry.grid(column=0, row=0, sticky=(N, E, W, S))
            #

            # Align everything
            align_rows_cols(self.S_label_frame)
            align_rows_cols(self.S_entry_frame)
            align_rows_cols(self.S_frame)

            align_rows_cols(self.S0_label_frame)
            align_rows_cols(self.S0_entry_frame)
            align_rows_cols(self.S0_frame)

            align_rows_cols(self.SG_label_frame)
            align_rows_cols(self.SG_entry_frame)
            align_rows_cols(self.SG_frame)

            align_rows_cols(self.T_label_frame)
            align_rows_cols(self.T_entry_frame)
            align_rows_cols(self.T_frame)

            align_rows_cols(self.L_label_frame)
            align_rows_cols(self.L_entry_frame)
            align_rows_cols(self.L_frame)

            align_rows_cols(self.u_label_frame)
            align_rows_cols(self.u_entry_frame)
            align_rows_cols(self.u_frame)

            align_rows_cols(self.G_label_frame)
            align_rows_cols(self.G_entry_frame)
            align_rows_cols(self.G_frame)

            align_rows_cols(self.root)
        except Exception as e:
            raise e
