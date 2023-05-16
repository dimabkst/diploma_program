from tkinter import ttk, N, W, E, S


def create_frame_label_entrie_frames(root, column: int, row: int, isRow: bool, style: str = "WhiteBg.TFrame",
                                     label_frame_style="WhiteBg.TFrame", entrie_frame_style="WhiteBg.TFrame",  padding: str = "3 3 12 12"):
    try:
        frame = ttk.Frame(root, padding=padding, style=style)
        frame.grid(column=column, row=row, sticky=(N, W, E, S))

        label_frame = ttk.Frame(frame, padding=padding,
                                style=label_frame_style)
        label_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        entries_frame = ttk.Frame(frame, padding=padding,
                                  style=entrie_frame_style)
        entries_frame.grid(column=1*isRow, row=1 * (not isRow),
                           sticky=(N, W, E, S))

        return frame, label_frame, entries_frame
    except Exception as e:
        raise e


def create_label_entrie_frames(root,
                               label_frame_column, label_frame_row,
                               entry_frame_column, entry_frame_row,
                               label_frame_style="WhiteBg.TFrame", entrie_frame_style="WhiteBg.TFrame",  padding: str = "3 3 12 12"):
    try:
        label_frame = ttk.Frame(root, padding=padding,
                                style=label_frame_style)
        label_frame.grid(column=label_frame_column, row=label_frame_row,
                         sticky=(N, W, E, S))

        entries_frame = ttk.Frame(root, padding=padding,
                                  style=entrie_frame_style)
        entries_frame.grid(column=entry_frame_column, row=entry_frame_row,
                           sticky=(N, W, E, S))

        return label_frame, entries_frame
    except Exception as e:
        raise e
