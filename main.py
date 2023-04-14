from view import View
from traceback import print_exc

if __name__ == "__main__":
    try:
        View("data.json")

    except Exception as e:
        print('Error occured:')
        print_exc(e)
