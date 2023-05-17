from re import search
from typing import Callable
from sympy.parsing import parse_expr
from sympy import lambdify
from sympy.abc import x, t


def heaviside_function(t_: float) -> float:
    if t_ > 0:
        return 1
    return 0


def parse_function(function_string: str) -> Callable:
    """

    :param function_string: function of two variables x,t string to be parsed
    :return: parsed function of two variables x, t
    """
    try:
        # create in view entry for heaviside
        heaviside_function_regex = r"Heaviside"
        heaviside_t_function_regex = r"Heaviside\(t\)"
        heaviside_x_function_regex = r"Heaviside\(x\)"

        heaviside = search(
            heaviside_function_regex, function_string)
        heaviside_t = search(
            heaviside_t_function_regex, function_string)
        heaviside_x = search(
            heaviside_x_function_regex, function_string)
        heaviside_t_or_x = heaviside_t or heaviside_x

        if heaviside_t and heaviside_x:
            raise Exception(
                'Only one Heaviside(t) or Heaviside(x) is supported')
        elif heaviside_t_or_x:
            if heaviside_t_or_x.start() != 0:
                raise Exception(
                    'Heaviside is only supported at the very beginning')

            function_string = function_string.replace(
                function_string[heaviside_t_or_x.start(): heaviside_t_or_x.end()], "")
            function_string = function_string[1:]
        elif heaviside:
            raise Exception('Only Heaviside(t) or Heaviside(x) is supported')

        def heaviside_to_use(x_: float, t_: float) -> float:
            if (heaviside_t):
                return heaviside_function(t_)
            elif (heaviside_x):
                return heaviside_function(x_)
            return 1  # no heaviside function is used

        sympy_function = parse_expr(function_string, transformations="all")

        # print(f'Sympy function: {sympy_function}')

        sympy_function = lambdify((x, t), sympy_function)

        def res(x_: float, t_: float) -> float:
            if (heaviside_to_use(x_, t_)):
                return sympy_function(x_, t_)
            return 0

        return res
    except Exception as e:
        raise e
