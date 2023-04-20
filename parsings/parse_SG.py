import numpy as np
import re


def parse_SG(SG_string: str) -> np.array:
    """

    :param SG_string: SG string to be parsed in format: [a0,b0] v [a1,b1] v ... v [a_last, b_last]
    :return: parsed np.array of SG in format: np.array([[a0, b0],...,[a_last, b_last]])
    """
    try:
        SG_str = SG_string.replace(' ', '')  # Remove all spaces
        atomic_SG_regex = r"\[[+-]?[0-9]+([.][0-9]+)?[,][+-]?[0-9]+([.][0-9]+)?\]"
        atomic_SG_regex_obj = re.compile(atomic_SG_regex)

        atomic_SGs_str_iterator = atomic_SG_regex_obj.finditer(SG_str)

        atomic_SGs = []
        for atomic_SG_match_object in atomic_SGs_str_iterator:
            atomic_SG_str = atomic_SG_match_object[0]  # String that looks like: [constant1, constant2]

            atomic_SG_constant1_str = ""
            atomic_SG_constant2_str = ""

            finding_constant1 = False
            finding_constant2 = False
            for char in atomic_SG_str:
                # Finding constant1
                if char == ",":  # Goes before below so we won't save it
                    finding_constant1 = False
                if finding_constant1:
                    atomic_SG_constant1_str += char
                if char == "[":  # Goes after upper so we won't save it
                    finding_constant1 = True

                # Finding constant2
                if char == "]":  # Goes before below so we won't save it
                    finding_constant2 = False
                if finding_constant2:
                    atomic_SG_constant2_str += char
                if char == ",":  # Goes after upper so we won't save it
                    finding_constant2 = True

            atomic_SG_constant1 = float(atomic_SG_constant1_str)
            atomic_SG_constant2 = float(atomic_SG_constant2_str)

            atomic_SGs.append([atomic_SG_constant1, atomic_SG_constant2])

        return np.array(atomic_SGs)
    except Exception as e:
        raise e
