import winsound


def beep(duration=1000, frequency=440):
    winsound.Beep(frequency, duration)


def error_beep():
    winsound.MessageBeep(-1)
