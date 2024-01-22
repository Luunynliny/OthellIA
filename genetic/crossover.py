import numpy as np


def one_point_crossover(
    p1: np.ndarray[np.float64, np.dtype[np.float64]],
    p2: np.ndarray[np.float64, np.dtype[np.float64]],
) -> tuple[
    np.ndarray[np.float64, np.dtype[np.float64]],
    np.ndarray[np.float64, np.dtype[np.float64]],
]:
    """Performs one-point crossover on two parent chromosomes and returns two new child
    chromosomes.

    New chromosomes are normalized to fit requirements.

    Args:
        p1 (np.ndarray[np.float64, np.dtype[np.float64]]): first parent chromosome.
        p2 (np.ndarray[np.float64, np.dtype[np.float64]]): second parent chromosome.

    Returns:
        tuple[np.ndarray[np.float64, np.dtype[np.float64]], np.ndarray[np.float64,
        np.dtype[np.float64]]]: child chromosomes.
    """
    rng = np.random.default_rng()

    point_index = rng.integers(1, len(p1))

    c1 = np.append(p2[:point_index], p1[point_index:])
    c2 = np.append(p1[:point_index], p2[point_index:])

    return c1 / sum(c1), c2 / sum(c2)


def two_point_crossover(
    p1: np.ndarray[np.float64, np.dtype[np.float64]],
    p2: np.ndarray[np.float64, np.dtype[np.float64]],
) -> tuple[
    np.ndarray[np.float64, np.dtype[np.float64]],
    np.ndarray[np.float64, np.dtype[np.float64]],
]:
    """Performs two-point crossover on two parent chromosomes and returns two new child
    chromosomes.

    New chromosomes are normalized to fit requirements.

    Args:
        p1 (np.ndarray[np.float64, np.dtype[np.float64]]): first parent chromosome.
        p2 (np.ndarray[np.float64, np.dtype[np.float64]]): second parent chromosome.

    Returns:
        tuple[np.ndarray[np.float64, np.dtype[np.float64]], np.ndarray[np.float64,
        np.dtype[np.float64]]]: child chromosomes.
    """
    rng = np.random.default_rng()

    point_indices = rng.choice(range(1, len(p1)), size=2, replace=False)
    point_indices.sort()

    i1, i2 = point_indices

    c1 = np.concatenate((p1[:i1], p2[i1:i2], p1[i2:]))
    c2 = np.concatenate((p2[:i1], p1[i1:i2], p2[i2:]))

    return c1 / sum(c1), c2 / sum(c2)


def uniform_crossover(
    p1: np.ndarray[np.float64, np.dtype[np.float64]],
    p2: np.ndarray[np.float64, np.dtype[np.float64]],
    p_swap: float,
) -> tuple[
    np.ndarray[np.float64, np.dtype[np.float64]],
    np.ndarray[np.float64, np.dtype[np.float64]],
]:
    """Performs uniform crossover on two parent chromosomes and returns two new child
    chromosomes.

    New chromosomes are normalized to fit requirements.

    Args:
        p1 (np.ndarray[np.float64, np.dtype[np.float64]]): first parent chromosome.
        p2 (np.ndarray[np.float64, np.dtype[np.float64]]): second parent chromosome.
        p_swap(float): probability of gene swapping.

    Returns:
        tuple[np.ndarray[np.float64, np.dtype[np.float64]], np.ndarray[np.float64,
        np.dtype[np.float64]]]: child chromosomes.
    """
    rng = np.random.default_rng()

    binary_mask = rng.choice([0, 1], size=len(p1), p=[1 - p_swap, p_swap])

    c1 = p1.copy()
    c2 = p2.copy()

    for i, b in enumerate(binary_mask):
        if b == 0:
            continue

        c1[i], c2[i] = c2[i], c1[i]

    return c1 / sum(c1), c2 / sum(c2)
