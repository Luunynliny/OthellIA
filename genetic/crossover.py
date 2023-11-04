import numpy as np


def one_point_crossover(
    p1: np.ndarray, p2: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Performs one-point crossover on two parent chromosomes and retuns two new child
    chromosomes.

    New chromosomes are normalized to fit requirements.

    Args:
        p1 (np.ndarray): first parent chromosome.
        p2 (np.ndarray): second parent chromosome.

    Returns:
        tuple[np.ndarray, np.ndarray]: child chromosomes.
    """
    rng = np.random.default_rng()

    point_index = rng.integers(1, len(p1))

    c1 = np.append(p2[:point_index], p1[point_index:])
    c2 = np.append(p1[:point_index], p2[point_index:])

    return c1 / sum(c1), c2 / sum(c2)
