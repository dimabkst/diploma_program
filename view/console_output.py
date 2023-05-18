import logging
from tkinter import N, E, W, S, scrolledtext
from .utils import TextHandler, create_grid_frame


class console_output:

    def __init__(self, root):
        try:
            # Frames
            self.root = create_grid_frame(
                root=root, column=0, row=0, style="TopWhiteBg.TFrame")

            self.console_frame = create_grid_frame(
                root=self.root, column=0, row=0, style="WhiteBg.TFrame")

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
