import logging
from tkinter import N, E, W, S, scrolledtext
from tkinter.ttk import Frame
from .utils import TextHandler


class console_output:

    def __init__(self, root):
        try:
            # Frames
            self.root = Frame(
                root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
            self.root.grid(column=0, row=0, sticky=(N, W, E, S))

            self.console_frame = Frame(
                self.root, style="WhiteBg.TFrame", padding="3 3 12 12")
            self.console_frame.grid(column=0, row=0, sticky=(N, W, E, S))

            # Console ScrolledText widget
            self.console_widget = scrolledtext.ScrolledText(
                self.console_frame, state='disabled')
            self.console_widget.grid(column=0, row=0, sticky=(N, W, E, S))

            text_handler = TextHandler(self.console_widget)

            # Logging configuration
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s')

            # Add the handler to logger
            logger = logging.getLogger()
            logger.addHandler(text_handler)
        except Exception as e:
            raise e
