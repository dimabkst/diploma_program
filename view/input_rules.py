from tkinter import N, E, W, S, PhotoImage
from tkinter.ttk import Frame, Label


class input_rules:

    def __init__(self, root):
        try:
            font = ("Arial", 14)

            # Frames
            self.root = Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.sets = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.sets.grid(column=0, row=0, sticky=(N, W, E, S))

            self.numbers = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.numbers.grid(column=0, row=1, sticky=(N, W, E, S))

            self.points = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.points.grid(column=1, row=1, sticky=(N, W, E, S))

            self.operators = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.operators.grid(column=0, row=2, sticky=(N, W, E, S))

            self.derivatives = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.derivatives.grid(column=1, row=2, sticky=(N, W, E, S))

            self.functions = Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.functions.grid(column=0, row=3, sticky=(N, W, E, S))

            # Labels and image
            Label(self.sets,
                  text="""Множини S, S0, SG повинні мати вигляд [a_0,b_0]x[a_1,b_1]x[a_2,b_2]x...\n\nТут a_i, b_i - числа, для яких b_i < a_i+1, а x - довільний, крім дужок [], роздільник.""",
                  font=font,
                  style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            Label(self.numbers, text="""YrlG, Yij - довільні числа.\n\nT - довільне число більше 0.\n\nR0, L0, RG, LG, I, Ji, кількість векторів v(x,t) - довільні натуральні числа. \n\nТочність обчислення інтегралів - довільне додатне число не нижче 5e-29. \n\nРозмірність сітки графіка - довільне натуральне число. \n\nМежі осей графіка X0, X1, T0, T1 - довільні числа для яких: X0 < X1, T0 < T1.""",
                  font=font,
                  style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            Label(self.points,
                  text="""xl0 - довільне число, таке, що xl0 є S0.\n\nslG, sij - точки вигляду (a,b) є SG x [0, T].""",
                  font=font,
                  style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            Label(self.operators,
                  text="""Оператори L, Lr0, LrG, Lij задаються у вигляді довільної лінійної комбінації частинних похідних.""",
                  font=font,
                  style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))

            Label(self.derivatives,
                  text="""Формат вводу частинних похідних:""",
                  font=font,
                  style="WhiteBg.TLabel") \
                .grid(column=0, row=1, sticky=(N, E, W, S))

            derivative_format_image = PhotoImage(
                file="./assets/derivative.gif")
            derivative_format_image_label = Label(
                self.derivatives,
                image=derivative_format_image,
                style="WhiteBg.TLabel")
            derivative_format_image_label.image = derivative_format_image
            derivative_format_image_label.grid(
                column=0, row=2, sticky=(N, E, W, S))

            Label(self.functions,
                  text="""Функції u(x,t), G(x,t), v(x,t) мають бути функціями двох змінних x,t та можуть мати довільний вигляд, який сприймає бібліотека SymPy.\n\nЄ можливість використати функцію Гевісайда Heaviside(), але лише на початку задання функції та лише від аргументів x або t.""",
                  font=font,
                  style="WhiteBg.TLabel") \
                .grid(column=0, row=0, sticky=(N, E, W, S))
        except Exception as e:
            raise e
