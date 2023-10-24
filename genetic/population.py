import numpy as np


def generate_random_chromosome() -> np.ndarray:
    """Returns a random chromosome.

    Returns:
        np.ndarray: a chromosome.
    """
    weights = np.random.rand(6)
    return weights / sum(weights)


def generate_random_population(size: int) -> np.ndarray:
    """Returns a list of random chromosomes.

    Args:
        size (int): number of chromosomes.

    Returns:
        np.ndarray: a list of chromosomes.
    """
    return np.array([generate_random_chromosome() for _ in range(size)])
