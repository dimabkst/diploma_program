from typing import List


def validate_stock_problem_input(alpha: float, beta: float, gamma: float,
                                 a: float, b: float, T: float,
                                 I: int, xi_list: List[float],
                                 J: int, tj_list: List[float],
                                 K: int, xk_list: List[float], tk_list: List[float], uk_list: List[float]) -> None:
    try:
        if a <= 0:
            raise Exception('a should be positive number')
        if a >= b:
            raise Exception('b should be greater than a')

        if T <= 0:
            raise Exception('T should be positive number')

        if I <= 0:
            raise Exception('I should be positive number')
        if len(xi_list) != I:
            raise Exception('List of xi should have length of I')
        for xi in xi_list:
            if not a <= xi <= b:
                raise Exception('xi should be in [a, b] segment')

        if J <= 0:
            raise Exception('J should be positive number')
        if len(tj_list) != J:
            raise Exception('List of tj should have length of J')
        for tj in tj_list:
            if not 0 <= tj <= T:
                raise Exception('tj should be in [0, T] segment')

        if K <= 0:
            raise Exception('K should be positive number')
        if len(xk_list) != K:
            raise Exception('List of xk should have length of K')
        for xk in xk_list:
            if not a <= xk <= b:
                raise Exception('xk should be in [a, b] segment')
        if len(tk_list) != K:
            raise Exception('List of tk should have length of K')
        for tk in tk_list:
            if not 0 <= tk <= T:
                raise Exception('tk should be in [0, T] segment')
        if len(uk_list) != K:
            raise Exception('List of uk should have length of K')
    except Exception as e:
        raise e
