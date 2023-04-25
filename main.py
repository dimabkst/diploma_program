from view import View
from traceback import print_exc
from parsings import parse_function

if __name__ == "__main__":
    try:
        # USE exp not e in view
        View("data.json")

    except Exception as e:
        print('Error occured:')
        print_exc(e)
