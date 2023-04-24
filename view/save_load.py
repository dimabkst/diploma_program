from tkinter import *
from tkinter import ttk
import fnmatch
import os


class save_load:

    def __init__(self, root, file_path, save_command, load_command):
        try:
            self.save_command = save_command
            self.load_command = load_command

            self.file_path = file_path
            self.save_file_prefix = "./saves/save"
            self.save_file_suffix = "." + file_path.split('.')[-1]
            self.saves_absolute_path = os.path.abspath(
                f'{"/".join(self.save_file_prefix.split("/")[:-1])}')
            self.current_save_number = \
                len(fnmatch.filter(os.listdir(self.saves_absolute_path),
                                   f'{self.save_file_prefix.split("/")[-1]}*{self.save_file_suffix}'))

            self.save_file_path = self.save_file_prefix + \
                str(self.current_save_number) + self.save_file_suffix

            s = ttk.Style()
            s.configure("TopWhiteBg.TFrame", background="white",
                        borderwidth=5, relief='raised')
            s.configure("VectorWhiteBg.TFrame", background="white",
                        borderwidth=5, relief="solid")
            s.configure("WhiteBg.TFrame", background="white")
            s.configure("WhiteBg.TLabel", background="white")

            # Frames
            self.root = ttk.Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.save_frame = ttk.Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.save_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            self.load_frame = ttk.Frame(
                self.root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.load_frame.grid(column=1, row=0, sticky=(N, W, E, S))
            #

            # Save button
            self.save_button = ttk.Button(self.save_frame, text="Зберегти введені дані",
                                          command=self.changed_save_command)
            self.save_button.grid(column=0, row=0, sticky=(N, W, E, S))
            #

            # Load buttons
            self.load_buttons = []
            self.delete_buttons = []
            for i in range(self.current_save_number):
                load_button = ttk.Button(self.load_frame, text=f'Збереження №{i + 1}',
                                         command=lambda i=i: self.load_command(
                                             self.save_file_prefix + str(i + 1) + self.save_file_suffix))
                load_button.grid(column=0, row=i, sticky=(N, W, E, S))

                delete_button = ttk.Button(self.load_frame, text=f'Видалити збереження №{i + 1}',
                                           command=lambda i=i: self.delete_save(i + 1))
                delete_button.grid(column=1, row=i, sticky=(N, W, E, S))

                self.load_buttons.append(load_button)
                self.delete_buttons.append(delete_button)
            #

            # Align
            self.align_rows_cols(self.save_frame)
            self.align_rows_cols(self.load_frame)

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

    def align_rows_cols_after_row_deleting(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num - 1):
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_rowconfigure(rows_num - 1, weight=0)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)

    def changed_save_command(self):
        try:
            self.current_save_number += 1
            self.change_save_file_path()
            self.change_and_show_load()

            self.save_command(self.save_file_path)
        except Exception as e:
            raise e

    def change_save_file_path(self):
        try:
            self.save_file_path = self.save_file_prefix + \
                str(self.current_save_number) + self.save_file_suffix
        except Exception as e:
            raise e

    def change_and_show_load(self):
        try:
            load_button = ttk.Button(self.load_frame, text=f'Збереження №{self.current_save_number}',
                                     command=lambda i=self.current_save_number: self.load_command(
                                         self.save_file_prefix + str(i) + self.save_file_suffix))
            load_button.grid(
                column=0, row=self.current_save_number - 1, sticky=(N, W, E, S))
            self.load_buttons.append(load_button)

            delete_button = ttk.Button(self.load_frame, text=f'Видалити збереження №{self.current_save_number}',
                                       command=lambda i=self.current_save_number: self.delete_save(i))
            delete_button.grid(
                column=1, row=self.current_save_number - 1, sticky=(N, W, E, S))
            self.delete_buttons.append(delete_button)

            self.align_rows_cols(self.load_frame)
        except Exception as e:
            raise e

    def delete_save(self, save_number: int):
        try:
            # Check save number
            if save_number > len(self.load_buttons) or save_number < 1:
                raise Exception("There is no such save file")

            # Delete wanted save file
            os.remove(self.save_file_prefix +
                      str(save_number) + self.save_file_suffix)

            # Decrement numbers in names of save files that go after deleted one
            for i in range(save_number, len(self.load_buttons)):
                os.rename(self.save_file_prefix + str(i + 1) + self.save_file_suffix,
                          self.save_file_prefix + str(i) + self.save_file_suffix)

            # Delete last load and delete buttons, because there won't be such save file after previous decrementing
            self.load_buttons[-1].destroy()
            self.load_buttons.pop()

            self.delete_buttons[-1].destroy()
            self.delete_buttons.pop()

            # For future saves
            self.current_save_number -= 1
            self.change_save_file_path()

            # Align buttons
            self.align_rows_cols_after_row_deleting(self.load_frame)
        except Exception as e:
            raise e
