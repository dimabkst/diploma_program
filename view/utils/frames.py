from tkinter import N, W, E, S
from tkinter.ttk import Frame


def create_grid_frame(root, column, row, style, sticky=(N, W, E, S), padding="3 3 12 12"):
    try:
        frame = Frame(root, padding=padding, style=style)

        frame.grid(column=column, row=row, sticky=sticky)

        return frame
    except Exception as e:
        raise e


def create_frame_label_entrie_frames(root, column: int, row: int, isRow: bool, style: str = "WhiteBg.TFrame",
                                     label_frame_style="WhiteBg.TFrame", entrie_frame_style="WhiteBg.TFrame",  padding: str = "3 3 12 12"):
    try:
        frame = create_grid_frame(
            root=root, column=column, row=row, style=style, padding=padding)

        label_frame = create_grid_frame(
            root=frame, column=0, row=0, style=label_frame_style, padding=padding)

        entries_frame = create_grid_frame(
            root=frame, column=1*isRow, row=1 * (not isRow), style=entrie_frame_style, padding=padding)

        return frame, label_frame, entries_frame
    except Exception as e:
        raise e


def create_label_entrie_frames(root,
                               label_frame_column, label_frame_row,
                               entry_frame_column, entry_frame_row,
                               label_frame_style="WhiteBg.TFrame", entrie_frame_style="WhiteBg.TFrame",  padding: str = "3 3 12 12"):
    try:
        label_frame = create_grid_frame(
            root=root, column=label_frame_column, row=label_frame_row, style=label_frame_style, padding=padding)

        entries_frame = create_grid_frame(
            root=root, column=entry_frame_column, row=entry_frame_row, style=entrie_frame_style, padding=padding)

        return label_frame, entries_frame
    except Exception as e:
        raise e
