import numpy as np
import re


def parse_S0(S0_string: str) -> np.array:
    """

    :param S0_string: S0 string to be parsed in format: [a0,b0] v [a1,b1] v ... v [a_last, b_last]
    :return: parsed np.array of S0 in format: np.array([[a0, b0],...,[a_last, b_last]])
    """
    try:
        S0_str = S0_string.replace(' ', '')  # Remove all spaces
        atomic_S0_regex = r"\[[+-]?[0-9]+([.][0-9]+)?[,][+-]?[0-9]+([.][0-9]+)?\]"
        atomic_S0_regex_obj = re.compile(atomic_S0_regex)

        atomic_S0s_str_iterator = atomic_S0_regex_obj.finditer(S0_str)

        atomic_S0s = []
        for atomic_S0_match_object in atomic_S0s_str_iterator:
            atomic_S0_str = atomic_S0_match_object[0]  # String that looks like: [constant1, constant2]

            atomic_S0_constant1_str = ""
            atomic_S0_constant2_str = ""

            finding_constant1 = False
            finding_constant2 = False
            for char in atomic_S0_str:
                # Finding constant1
                if char == ",":  # Goes before below so we won't save it
                    finding_constant1 = False
                if finding_constant1:
                    atomic_S0_constant1_str += char
                if char == "[":  # Goes after upper so we won't save it
                    finding_constant1 = True

                # Finding constant2
                if char == "]":  # Goes before below so we won't save it
                    finding_constant2 = False
                if finding_constant2:
                    atomic_S0_constant2_str += char
                if char == ",":  # Goes after upper so we won't save it
                    finding_constant2 = True

            atomic_S0_constant1 = float(atomic_S0_constant1_str)
            atomic_S0_constant2 = float(atomic_S0_constant2_str)

            atomic_S0s.append([atomic_S0_constant1, atomic_S0_constant2])

        return np.array(atomic_S0s)
    except Exception as e:
        raise e
