from typing import Callable
from scipy.misc import derivative
import re


def atomic_differential_operator(constant: float, var: int = 0, der_order: int = 1) -> Callable:
    def derivative_of_func(func: Callable) -> Callable:
        def derivative_of_func_in_point(*point) -> float:
            args = list(point[:])

            def wraps(x):
                args[var] = x
                return func(*args)

            return constant * derivative(func=wraps, x0=point[var], dx=1e-6, n=der_order)

        return derivative_of_func_in_point

    return derivative_of_func


def parse_operator(operator_string: str) -> Callable:
    """

    :param operator_string: string to be parsed in format c * d[v, k] = c * d^k/dv^k
    :return: differential operator that takes a function and
        returns a needed combination of partial derivatives of that function
    """
    try:
        op_str = operator_string.replace(' ', '')  # Remove all spaces
        atomic_op_regex = r"[+-]?[0-9]+([.][0-9]+)?\*[d]\[(x|t)[,][1-9][0-9]*\]"
        atomic_op_regex_obj = re.compile(atomic_op_regex)

        atomic_ops_str_iterator = atomic_op_regex_obj.finditer(op_str)

        atomic_ops = []
        for atomic_op_match_object in atomic_ops_str_iterator:
            atomic_op_str = \
                atomic_op_match_object[
                    0]  # String that looks like: c*d[x,n] or c*d[t,n]. c - float const, n - int const

            atomic_op_constant_str = ""
            atomic_op_der_order_str = ""
            atomic_op_var = -1

            finding_constant = True
            finding_der_order = False
            for char in atomic_op_str:
                # Finding constant
                if char == "*":
                    finding_constant = False
                if finding_constant:
                    atomic_op_constant_str += char

                # Finding var
                if char == "x":
                    atomic_op_var = 0
                elif char == "t":
                    atomic_op_var = 1

                # Finding derivative order
                if char == "]":  # It goes before below so we won't save ]
                    finding_der_order = False
                if finding_der_order:
                    atomic_op_der_order_str += char
                if char == ",":  # It goes after upper check so we won't save ,
                    finding_der_order = True

            atomic_op_constant = float(atomic_op_constant_str)
            atomic_op_der_order = int(atomic_op_der_order_str)

            atomic_ops.append(atomic_differential_operator(
                atomic_op_constant, atomic_op_var, atomic_op_der_order))

            # print(f'Constant: {atomic_op_constant}, var: {atomic_op_var}, der_order: {atomic_op_der_order}')

        def differential_operator(func: Callable) -> Callable:
            def differential_operator_of_func_in_point(*point) -> float:
                res = sum([atomic_diff_op(func)(*point)
                          for atomic_diff_op in atomic_ops])

                return res

            return differential_operator_of_func_in_point

        return differential_operator
    except Exception as e:
        print(e)
