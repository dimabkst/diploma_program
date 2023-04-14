from tkinter import *
from tkinter import ttk

ENTRY_WIDTH = 10


class problem_conditions_input:

    def __init__(self, root):
        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
        s.configure("WhiteBg.TFrame", background="white")
        s.configure("WhiteBg.TLabel", background="white")

        # Frames
        self.root = ttk.Frame(root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.root.grid(column=0, row=0, sticky=(N, W, E, S))

        self.S0_frame = ttk.Frame(self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.S0_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.T_frame = ttk.Frame(self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.T_frame.grid(column=0, row=1, sticky=(N, W, E, S))

        self.L_frame = ttk.Frame(self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.L_frame.grid(column=0, row=2, sticky=(N, W, E, S))

        self.u_frame = ttk.Frame(self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.u_frame.grid(column=0, row=3, sticky=(N, W, E, S))

        self.G_frame = ttk.Frame(self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.G_frame.grid(column=0, row=4, sticky=(N, W, E, S))

        # S0_input
        self.S0_label_frame = ttk.Frame(self.S0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.S0_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.S0_entry_frame = ttk.Frame(self.S0_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.S0_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.S0_var = StringVar()
        self.S0_var.set("[0, 1]")

        ttk.Label(self.S0_label_frame, text="S0 =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))

        self.S0_entry = ttk.Entry(self.S0_entry_frame, width=ENTRY_WIDTH, textvariable=self.S0_var)
        self.S0_entry_hsb = ttk.Scrollbar(self.S0_entry_frame, orient=HORIZONTAL, command=self.S0_entry.xview)
        self.S0_entry.configure(xscrollcommand=self.S0_entry_hsb.set)
        self.S0_entry_hsb.grid(column=0, row=1, sticky=(E, W))
        self.S0_entry.grid(column=0, row=0, sticky=(N, E, W, S))
        #

        # T_input
        self.T_label_frame = ttk.Frame(self.T_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.T_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.T_entry_frame = ttk.Frame(self.T_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.T_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.T_var = StringVar()
        self.T_var.set("5")

        ttk.Label(self.T_label_frame, text="T =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))

        self.T_entry = ttk.Entry(self.T_entry_frame, width=ENTRY_WIDTH, textvariable=self.T_var)
        self.T_entry.grid(column=0, row=0, sticky=(N, E, W, S))
        #

        # L_input
        self.L_label_frame = ttk.Frame(self.L_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.L_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.L_entry_frame = ttk.Frame(self.L_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.L_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.L_format_frame = ttk.Frame(self.L_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.L_format_frame.grid(column=1, row=1, sticky=(N, W, E, S))

        self.L_var = StringVar()
        self.L_var.set("1*d[t,2]-16*d[x,2]")

        ttk.Label(self.L_label_frame, text="L(dx,dt) =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))

        self.L_entry = ttk.Entry(self.L_entry_frame, width=ENTRY_WIDTH, textvariable=self.L_var)
        self.L_entry.grid(column=0, row=0, sticky=(N, E, W, S))

        ttk.Label(self.L_format_frame, text="Формат вводу частинних похідних:", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))

        L_format_image = PhotoImage(file="./assets/derivative.gif")
        L_format_image_label = ttk.Label(self.L_format_frame, image=L_format_image, style="WhiteBg.TLabel")
        L_format_image_label.image = L_format_image
        L_format_image_label.grid(column=1, row=0, sticky=(N, E, W, S))
        #

        # u_input
        self.u_label_frame = ttk.Frame(self.u_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.u_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.u_entry_frame = ttk.Frame(self.u_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.u_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.u_var = StringVar()
        self.u_var.set("x^3+exp(t)")

        ttk.Label(self.u_label_frame, text="u(x,t) =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))

        self.u_entry = ttk.Entry(self.u_entry_frame, width=ENTRY_WIDTH, textvariable=self.u_var)
        self.u_entry.grid(column=0, row=0, sticky=(N, E, W, S))
        #

        # G_input
        self.G_label_frame = ttk.Frame(self.G_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.G_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.G_entry_frame = ttk.Frame(self.G_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.G_entry_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.G_var = StringVar()
        self.G_var.set("x**2 + t**3")

        ttk.Label(self.G_label_frame, text="G(x,t) =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))

        self.G_entry = ttk.Entry(self.G_entry_frame, width=ENTRY_WIDTH, textvariable=self.G_var)
        self.G_entry_hsb = ttk.Scrollbar(self.G_entry_frame, orient=HORIZONTAL, command=self.G_entry.xview)
        self.G_entry.configure(xscrollcommand=self.G_entry_hsb.set)
        self.G_entry_hsb.grid(column=0, row=1, sticky=(E, W))
        self.G_entry.grid(column=0, row=0, sticky=(N, E, W, S))
        #

        # Align everything
        self.align_rows_cols(self.S0_label_frame)
        self.align_rows_cols(self.S0_entry_frame)
        self.align_rows_cols(self.S0_frame)

        self.align_rows_cols(self.T_label_frame)
        self.align_rows_cols(self.T_entry_frame)
        self.align_rows_cols(self.T_frame)

        self.align_rows_cols(self.L_label_frame)
        self.align_rows_cols(self.L_entry_frame)
        self.align_rows_cols(self.L_frame)

        self.align_rows_cols(self.u_label_frame)
        self.align_rows_cols(self.u_entry_frame)
        self.align_rows_cols(self.u_frame)

        self.align_rows_cols(self.G_label_frame)
        self.align_rows_cols(self.G_entry_frame)
        self.align_rows_cols(self.G_frame)

        self.align_rows_cols(self.root)

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
