import numpy as np


def generate_random_chromosome() -> (
    np.ndarray[np.float64, np.dtype[np.float64]]
):
    """Returns a random chromosome.

    Returns:
        np.ndarray[np.float64, np.dtype[np.float64]]: a chromosome.
    """
    rng = np.random.default_rng()

    weights = rng.random(6)
    return np.array(weights / sum(weights))


def generate_random_population(
    size: int,
) -> np.ndarray[np.float64, np.dtype[np.float64]]:
    """Returns a list of random chromosomes.

    Args:
        size (int): number of chromosomes.

    Returns:
        np.ndarray[np.float64, np.dtype[np.float64]]: a list of chromosomes.
    """
    return np.array([generate_random_chromosome() for _ in range(size)])
