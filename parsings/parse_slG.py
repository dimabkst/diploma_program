from parsings import parse_number


def parse_slG(slG_string: str) -> list:
    """

    :param slG_string: string of slG point to parse that look like (c1, c2)
    :return: list that represents parsed slG point
    """
    try:
        slG_str = slG_string.replace(' ', '')  # Remove all spaces
        slG_parts = slG_str.split(',')
        slG_constant1_str = slG_parts[0][1:]  # Remove (
        slG_constant2_str = slG_parts[1][:-1]  # Remove )

        return [parse_number(slG_constant1_str), parse_number(slG_constant2_str)]
    except Exception as e:
        raise e
