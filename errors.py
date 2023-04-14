class Error(Exception):
    def __str__(self) -> str:
        return 'Program aborted\n'


class NoNameError(Error):
    def __init__(self, e):
        self.e = e

    def __str__(self) -> str:
        return f'{self.e}'
