def parse_float_number(float_number_string: str) -> float:
    """

    :param float_number_string: string of float number to parse
    :return: parsed integer number
    """
    try:
        return float(float_number_string)
    except Exception as e:
        raise e
