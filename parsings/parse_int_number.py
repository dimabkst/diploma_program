def parse_int_number(int_number_string: str) -> int:
    """

    :param int_number_string: string of integer number to parse
    :return: parsed integer number
    """
    try:
        return int(int_number_string)
    except Exception as e:
        raise e
