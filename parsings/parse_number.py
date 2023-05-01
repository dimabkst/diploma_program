from parsings import parse_int_number, parse_float_number


def parse_number(number_string: str):
    """

    :param number_string: string of number to parse
    :return: parsed number
    """
    try:
        if '.' or 'e' in number_string:
            return parse_float_number(number_string)
        else:
            return parse_int_number(number_string)
    except Exception as e:
        raise e
