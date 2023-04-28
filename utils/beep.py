import winsound


def beep(duration=1000, frequency=440):
    winsound.Beep(frequency, duration)
