def validate_alpha_beta_gamma_input(mu: float, sigma: float, b: float, c: float) -> None:
    try:
        if mu <= 0:
            raise Exception('mu should be positive number')

        if sigma <= 0:
            raise Exception('sigma should be positive number')

        if b < 0:
            raise Exception('b should be non-negative number')

    except Exception as e:
        raise e
