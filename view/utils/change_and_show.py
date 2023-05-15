from tkinter import *
from tkinter import ttk


def change_and_show_1dim(var_to_watch,
                         vars_to_cas, vars_to_cas_callback, vars_to_cas_new_value_function,
                         labels_to_cas, labels_to_cas_text_function, labels_to_cas_style,
                         entries_to_cas, entries_to_cas_width, entries_state,
                         frame_to_cas,
                         isRow):
    try:
        if var_to_watch.get() and int(var_to_watch.get()) > 0:
            old_count = len(vars_to_cas)
            for i in range(max(old_count, int(var_to_watch.get() or 0))):
                if i >= min(old_count, int(var_to_watch.get() or 0)):
                    if old_count > int(var_to_watch.get() or 0):
                        vars_to_cas = vars_to_cas[0:i]

                        for ii in range(i, old_count):
                            labels_to_cas[ii].destroy()
                            entries_to_cas[ii].destroy()

                        labels_to_cas = labels_to_cas[0:i]
                        entries_to_cas = entries_to_cas[0:i]
                        break
                    else:
                        vars_to_cas.append(StringVar())

                        labels_to_cas.append(
                            ttk.Label(frame_to_cas, text=labels_to_cas_text_function(i), style=labels_to_cas_style))
                        entries_to_cas.append(
                            ttk.Entry(frame_to_cas, width=entries_to_cas_width,
                                      textvariable=vars_to_cas[i], state=entries_state))

                        vars_to_cas[i].set(vars_to_cas_new_value_function(i))
                        vars_to_cas[i].trace(
                            "w", lambda name, index, mode: vars_to_cas_callback(name, index, mode))
                        labels_to_cas[i].grid(
                            row=i*isRow, column=i*(not isRow), sticky=(N, W, E, S))
                        entries_to_cas[i].grid(
                            row=1*(not isRow) + i*isRow, column=1*isRow + i*(not isRow), sticky=(N, W, E, S))

        return vars_to_cas, labels_to_cas, entries_to_cas
    except Exception as e:
        raise e


def change_and_show_2dim(row_var_to_watch, col_var_to_watch,
                         vars_to_cas, vars_to_cas_new_value_function,
                         labels_to_cas, labels_to_cas_text_function, labels_to_cas_style,
                         entries_to_cas, entries_to_cas_width, entries_state,
                         frame_to_cas,
                         additional_conditions=True):
    try:
        if (col_var_to_watch.get() and int(col_var_to_watch.get()) > 0) and (
                row_var_to_watch.get() and int(row_var_to_watch.get()) > 0) \
                and additional_conditions:

            old_row = len(vars_to_cas)
            old_col = len(vars_to_cas[0])

            for i in range(max(old_row, int(row_var_to_watch.get() or 0))):
                if i >= min(old_row, int(row_var_to_watch.get() or 0)):
                    if old_row > int(row_var_to_watch.get() or 0):
                        vars_to_cas = vars_to_cas[0:i]

                        for ii in range(i, old_row):
                            for k in range(int(col_var_to_watch.get() or 0)):
                                labels_to_cas[ii][k].destroy()
                                entries_to_cas[ii][k].destroy()

                        labels_to_cas = labels_to_cas[0:i]
                        entries_to_cas = entries_to_cas[0:i]
                        break
                    else:
                        vars_to_cas.append(
                            [StringVar() for _ in range(int(col_var_to_watch.get() or 0))])

                        labels_to_cas.append([
                            ttk.Label(frame_to_cas,
                                      text=labels_to_cas_text_function(i, k), style=labels_to_cas_style) for k in
                            range(int(col_var_to_watch.get() or 0))])
                        entries_to_cas.append([
                            ttk.Entry(frame_to_cas, width=entries_to_cas_width,
                                      textvariable=vars_to_cas[i][k], state=entries_state) for k in
                            range(int(col_var_to_watch.get() or 0))])

                        for k in range(int(col_var_to_watch.get() or 0)):
                            vars_to_cas[i][k].set(
                                vars_to_cas_new_value_function(i, k))
                            labels_to_cas[i][k].grid(
                                row=i, column=k * 2, sticky=(N, W, E, S))
                            entries_to_cas[i][k].grid(
                                row=i, column=k * 2 + 1, sticky=(N, W, E, S))

                for j in range(max(old_col, int(col_var_to_watch.get() or 0))):
                    if j >= min(old_col, int(col_var_to_watch.get() or 0)):
                        if old_col > int(col_var_to_watch.get() or 0):
                            vars_to_cas[i] = vars_to_cas[i][0:j]
                            for k in range(j, old_col):
                                labels_to_cas[i][k].destroy()
                                entries_to_cas[i][k].destroy()
                            labels_to_cas[i] = labels_to_cas[i][0:j]
                            entries_to_cas[i] = entries_to_cas[i][0:j]
                            break
                        else:
                            vars_to_cas[i].append(StringVar())
                            vars_to_cas[i][j].set(
                                vars_to_cas_new_value_function(i, j))

                            labels_to_cas[i].append(
                                ttk.Label(frame_to_cas,
                                          text=labels_to_cas_text_function(i, j), style=labels_to_cas_style))
                            labels_to_cas[i][j].grid(
                                row=i, column=j * 2, sticky=(N, W, E, S))

                            entries_to_cas[i].append(
                                ttk.Entry(frame_to_cas, width=entries_to_cas_width,
                                          textvariable=vars_to_cas[i][j], state=entries_state))
                            entries_to_cas[i][j].grid(
                                row=i, column=j * 2 + 1, sticky=(N, W, E, S))
                    else:
                        labels_to_cas[i][j].destroy()
                        labels_to_cas[i][j] = ttk.Label(frame_to_cas,
                                                        text=labels_to_cas_text_function(i, j), style=labels_to_cas_style)
                        labels_to_cas[i][j].grid(
                            row=i, column=j * 2, sticky=(N, W, E, S))

        return vars_to_cas, labels_to_cas, entries_to_cas
    except Exception as e:
        raise e


def change_and_show_2dim_desired(row_var_to_watch, col_vars_to_watch,
                                 vars_to_cas, vars_to_cas_callback, vars_to_cas_new_value_function,
                                 labels_to_cas, labels_to_cas_text_function, labels_to_cas_style,
                                 entries_to_cas, entries_to_cas_width, entries_state,
                                 frame_to_cas,
                                 additional_conditions=True):
    try:
        if (row_var_to_watch.get() and int(row_var_to_watch.get()) > 0)\
            and all([el.get() and int(el.get()) > 0 for el in col_vars_to_watch])\
                and additional_conditions:

            old_row = len(vars_to_cas)

            for i in range(max(old_row, int(row_var_to_watch.get() or 0))):
                try:
                    old_col = len(vars_to_cas[i])
                except IndexError:
                    old_col = 0

                if i >= min(old_row, int(row_var_to_watch.get() or 0)):
                    if old_row > int(row_var_to_watch.get() or 0):
                        vars_to_cas = vars_to_cas[0:i]

                        for ii in range(i, old_row):
                            for k in range(old_col):
                                labels_to_cas[ii][k].destroy()
                                entries_to_cas[ii][k].destroy()

                        labels_to_cas = labels_to_cas[0:i]
                        entries_to_cas = entries_to_cas[0:i]
                        break
                    else:
                        vars_to_cas.append(
                            [StringVar() for _ in range(int(col_vars_to_watch[i].get() or 0))])

                        labels_to_cas.append([
                            ttk.Label(frame_to_cas,
                                      text=labels_to_cas_text_function(i, k), style=labels_to_cas_style) for k in
                            range(int(col_vars_to_watch[i].get() or 0))])
                        entries_to_cas.append([
                            ttk.Entry(frame_to_cas, width=entries_to_cas_width,
                                      textvariable=vars_to_cas[i][k], state=entries_state) for k in
                            range(int(col_vars_to_watch[i].get() or 0))])

                        for k in range(int(col_vars_to_watch[i].get() or 0)):
                            vars_to_cas[i][k].set(
                                vars_to_cas_new_value_function(i, k))
                            vars_to_cas[i][k].trace(
                                "w", lambda name, index, mode: vars_to_cas_callback(name, index, mode))
                            labels_to_cas[i][k].grid(
                                row=i, column=k * 2, sticky=(N, W, E, S))
                            entries_to_cas[i][k].grid(
                                row=i, column=k * 2 + 1, sticky=(N, W, E, S))

                try:
                    old_col = len(vars_to_cas[i])
                except IndexError:
                    old_col = 0

                for j in range(max(old_col, int(col_vars_to_watch[i].get() or 0))):
                    if j >= min(old_col, int(col_vars_to_watch[i].get() or 0)):
                        if old_col > int(col_vars_to_watch[i].get() or 0):
                            vars_to_cas[i] = vars_to_cas[i][0:j]
                            for k in range(j, old_col):
                                labels_to_cas[i][k].destroy()
                                entries_to_cas[i][k].destroy()
                            labels_to_cas[i] = labels_to_cas[i][0:j]
                            entries_to_cas[i] = entries_to_cas[i][0:j]
                            break
                        else:
                            vars_to_cas[i].append(StringVar())
                            vars_to_cas[i][j].set(
                                vars_to_cas_new_value_function(i, j))
                            vars_to_cas[i][j].trace(
                                "w", lambda name, index, mode: vars_to_cas_callback(name, index, mode))

                            labels_to_cas[i].append(
                                ttk.Label(frame_to_cas,
                                          text=labels_to_cas_text_function(i, j), style=labels_to_cas_style))
                            labels_to_cas[i][j].grid(
                                row=i, column=j * 2, sticky=(N, W, E, S))

                            entries_to_cas[i].append(
                                ttk.Entry(frame_to_cas, width=entries_to_cas_width,
                                          textvariable=vars_to_cas[i][j], state=entries_state))
                            entries_to_cas[i][j].grid(
                                row=i, column=j * 2 + 1, sticky=(N, W, E, S))
                    else:
                        labels_to_cas[i][j].destroy()
                        labels_to_cas[i][j] = ttk.Label(frame_to_cas,
                                                        text=labels_to_cas_text_function(i, j), style=labels_to_cas_style)
                        labels_to_cas[i][j].grid(
                            row=i, column=j * 2, sticky=(N, W, E, S))

        return vars_to_cas, labels_to_cas, entries_to_cas
    except Exception as e:
        raise e
