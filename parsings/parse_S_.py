import numpy as np
import re


def parse_S_(S_string: str) -> np.array:
    """

    :param S_string: S_ string to be parsed in format: [a0,b0] v [a1,b1] v ... v [a_last, b_last]
    :return: parsed np.array of S_ in format: np.array([[a0, b0],...,[a_last, b_last]])
    """
    try:
        S_str = S_string.replace(' ', '')  # Remove all spaces
        atomic_S_regex = r"\[[+-]?[0-9]+([.][0-9]+)?[,][+-]?[0-9]+([.][0-9]+)?\]"
        atomic_S_regex_obj = re.compile(atomic_S_regex)

        atomic_Ss_str_iterator = atomic_S_regex_obj.finditer(S_str)

        atomic_S_s = []
        for atomic_S_match_object in atomic_Ss_str_iterator:
            # String that looks like: [constant1, constant2]
            atomic_S_str = atomic_S_match_object[0]

            atomic_S_constant1_str = ""
            atomic_S_constant2_str = ""

            finding_constant1 = False
            finding_constant2 = False
            for char in atomic_S_str:
                # Finding constant1
                if char == ",":  # Goes before below so we won't save it
                    finding_constant1 = False
                if finding_constant1:
                    atomic_S_constant1_str += char
                if char == "[":  # Goes after upper so we won't save it
                    finding_constant1 = True

                # Finding constant2
                if char == "]":  # Goes before below so we won't save it
                    finding_constant2 = False
                if finding_constant2:
                    atomic_S_constant2_str += char
                if char == ",":  # Goes after upper so we won't save it
                    finding_constant2 = True

            atomic_S_constant1 = float(atomic_S_constant1_str)
            atomic_S_constant2 = float(atomic_S_constant2_str)

            atomic_S_s.append([atomic_S_constant1, atomic_S_constant2])

        return np.array(atomic_S_s)
    except Exception as e:
        raise e
