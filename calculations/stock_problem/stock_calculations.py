from typing import Callable, List, Dict
from math import exp, log


def alpha_f(sigma: float, b: float) -> float:
    try:
        return (b * sigma ** 2) / 2
    except Exception as e:
        raise e


def beta_f(mu: float, sigma: float, b: float, c: float) -> float:
    try:
        return 2 * b * sigma ** 2 - c * sigma - mu
    except Exception as e:
        raise e


def gamma_f(mu: float, sigma: float, b: float, c: float) -> float:
    try:
        return b * sigma ** 2 - c * sigma - mu
    except Exception as e:
        raise e


def alpha_beta_gamma(mu: float, sigma: float, b: float, c: float) -> Dict[str, float]:
    try:
        return {"alpha": alpha_f(sigma, b), "beta": beta_f(mu, sigma, b, c), "gamma": gamma_f(mu, sigma, b, c)}
    except Exception as e:
        raise e


def C_f(alpha: float, beta: float) -> float:
    try:
        return beta - alpha
    except Exception as e:
        raise e


def x_f(z: float, tau: float, C: float, alpha: float) -> float:
    try:
        return exp(z - C * tau / alpha)
    except Exception as e:
        raise e


def t_f(tau: float, alpha: float) -> float:
    try:
        return tau / alpha
    except Exception as e:
        raise e


def z_f(x: float, t: float, C: float) -> float:
    try:
        return log(x) + C * t
    except Exception as e:
        raise e


def tau_f(t: float, alpha: float) -> float:
    try:
        return alpha * t
    except Exception as e:
        raise e


def u_f(y_f: Callable, alpha: float, beta: float, gamma: float) -> Callable:
    try:
        def res(x: float, t: float) -> float:
            return exp(gamma * t) * y_f(log(x) + (beta - alpha) * t, alpha * t)

        return res
    except Exception as e:
        raise e


def discrete_u_f(y: float, t: float, gamma: float) -> float:
    try:
        return y * exp(gamma * t)
    except Exception as e:
        raise e


def discrete_y_f(t: float, u: float, gamma: float) -> float:
    try:
        return u / exp(gamma * t)
    except Exception as e:
        raise e


def programm_T(T: float, alpha: float) -> float:
    try:
        return tau_f(T, alpha)
    except Exception as e:
        raise e


def programm_S_(a: float, b: float, T: float, C: float) -> List[float]:
    try:
        return [z_f(a, 0, C), z_f(b, T, C)]
    except Exception as e:
        raise e


def programm_s_(x_: List[float], t_: List[float], C: float, alpha: float) -> List[str]:
    return [f'({z_f(x_[_], t_[_], C)},{tau_f(t_[_], alpha)})' for _ in range(len(x_))]


def transform_stocks_problem(alpha: float, beta: float, gamma: float,
                             a: float, b: float, T: float,
                             I: int, xi_list: List[float],
                             J: int, tj_list: List[float],
                             K: int, xk_list: List[float], tk_list: List[float], uk_list: List[float]) -> Dict[str, float]:
    try:
        C = C_f(alpha, beta)

        res = {
            'S': str(programm_S_(a, b, T, C)),
            'S0': str(programm_S_(a, b, 0, C)),
            'SG': str(programm_S_(a, b, T, C)),
            'T': str(programm_T(T, alpha)),
            'L': '1*d[t,1]-1*d[x,2]',
            'u': '0',
            'G': 'Heaviside(t)*exp(-x^2/(4*t)) / sqrt(4 * pi * t)',
            'R0': '1',
            'L0': str(I),
            'Lr0_list': ['1*d[t,0]'],
            'xl0_list': [str(log(el)) for el in xi_list],
            'RG': '1',
            'LG': str(J),
            'LrG_list': ['1*d[x,0]'],
            'slG_list': programm_s_([a for _ in range(J)], tj_list, C, alpha),
            'YrlG_list': [['0' for _ in range(J)]],
            'I': '1',
            'Ji_list': [str(K)],
            'Li_list': ['1*d[x,0]'],
            'sij_list': [programm_s_(xk_list, tk_list, C, alpha)],
            'Yij_list': [[str(el) for el in [discrete_y_f(tk_list[k], uk_list[k], gamma) for k in range(len(uk_list))]]]
        }

        return res
    except Exception as e:
        raise e
