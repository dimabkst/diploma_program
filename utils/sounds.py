from winsound import Beep, MessageBeep


def beep(duration=1000, frequency=440):
    Beep(frequency, duration)


def error_beep():
    MessageBeep(-1)
