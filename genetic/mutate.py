import numpy as np


def swap(chromosome: np.ndarray) -> np.ndarray:
    """Performs swap mutation and returns the new chromosome state.

    Args:
        chromosome (np.ndarray): a chromosome.

    Returns:
        np.ndarray: mutated chromosome.
    """
    rng = np.random.default_rng()

    to_swap_indices = rng.choice(range(len(chromosome)), size=2, replace=False)

    i1, i2 = to_swap_indices

    mutated = chromosome.copy()
    mutated[i1], mutated[i2] = mutated[i2], mutated[i1]

    return mutated


def scramble(chromosome: np.ndarray) -> np.ndarray:
    """Performs scramble mutation and returns the new chromosome state.

    Args:
        chromosome (np.ndarray): a chromosome.

    Returns:
        np.ndarray: mutated chromosome.
    """
    rng = np.random.default_rng()

    to_scramble_indices = rng.choice(
        range(len(chromosome)), size=2, replace=False
    )
    to_scramble_indices.sort()

    i1, i2 = to_scramble_indices

    return np.concatenate(
        [
            chromosome[:i1],
            rng.shuffle(chromosome[i1 : i2 + 1]),
            chromosome[i2 + 1 :],
        ]
    )
