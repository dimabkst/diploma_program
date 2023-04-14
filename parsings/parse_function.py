from typing import Callable
from sympy.parsing import parse_expr
from sympy import lambdify
from sympy.abc import x, t


def parse_function(function_string: str) -> Callable:
    """

    :param function_string: function of two variables x,t string to be parsed
    :return: parsed function of two variables x, t
    """
    try:
        sympy_function = parse_expr(function_string, transformations="all")

        # print(f'Sympy function: {sympy_function}')

        return lambdify((x, t), sympy_function)
    except Exception as e:
        raise e
