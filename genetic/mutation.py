import numpy as np


def swap(
    chromosome: np.ndarray[np.float64, np.dtype[np.float64]]
) -> np.ndarray[np.float64, np.dtype[np.float64]]:
    """Performs swap mutation and returns the new chromosome state.

    Args:
        chromosome (np.ndarray[np.float64, np.dtype[np.float64]]): a chromosome.

    Returns:
        np.ndarray[np.float64, np.dtype[np.float64]]: mutated chromosome.
    """
    rng = np.random.default_rng()

    to_swap_indices = rng.choice(range(len(chromosome)), size=2, replace=False)

    i1, i2 = to_swap_indices

    mutated = chromosome.copy()
    mutated[i1], mutated[i2] = mutated[i2], mutated[i1]

    return mutated


def scramble(
    chromosome: np.ndarray[np.float64, np.dtype[np.float64]]
) -> np.ndarray[np.float64, np.dtype[np.float64]]:
    """Performs scramble mutation and returns the new chromosome state.

    Args:
        chromosome (np.ndarray[np.float64, np.dtype[np.float64]]): a chromosome.

    Returns:
        np.ndarray[np.float64, np.dtype[np.float64]]: mutated chromosome.
    """
    rng = np.random.default_rng()

    to_scramble_indices = rng.choice(
        range(len(chromosome)), size=2, replace=False
    )
    to_scramble_indices.sort()

    i1, i2 = to_scramble_indices

    shuffled = chromosome[i1 : i2 + 1].copy()
    rng.shuffle(shuffled)

    return np.concatenate(
        [
            chromosome[:i1],
            shuffled,
            chromosome[i2 + 1 :],
        ],
        axis=None,
    )


def inversion(
    chromosome: np.ndarray[np.float64, np.dtype[np.float64]]
) -> np.ndarray[np.float64, np.dtype[np.float64]]:
    """Performs inversion mutation and returns the new chromosome state.

    Args:
        chromosome (np.ndarray[np.float64, np.dtype[np.float64]]): a chromosome.

    Returns:
        np.ndarray[np.float64, np.dtype[np.float64]]: mutated chromosome.
    """
    rng = np.random.default_rng()

    to_inverse_indices = rng.choice(
        range(len(chromosome)), size=2, replace=False
    )
    to_inverse_indices.sort()

    i1, i2 = to_inverse_indices

    return np.concatenate(
        [
            chromosome[:i1],
            chromosome[i1 : i2 + 1][::-1],
            chromosome[i2 + 1 :],
        ],
        axis=None,
    )
