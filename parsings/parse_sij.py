from parsings import parse_number


def parse_sij(sij_string: str) -> list:
    """

    :param sij_string: string of sij point to parse that look like (c1, c2)
    :return: list that represents parsed sij point
    """
    try:
        sij_str = sij_string.replace(' ', '')  # Remove all spaces
        sij_parts = sij_str.split(',')
        sij_constant1_str = sij_parts[0][1:]  # Remove (
        sij_constant2_str = sij_parts[1][:-1]  # Remove )

        return [parse_number(sij_constant1_str), parse_number(sij_constant2_str)]
    except Exception as e:
        raise e
