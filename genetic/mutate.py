import numpy as np


def swap(chromosome: np.ndarray) -> np.ndarray:
    """Perform swap mutation and returns the new chromosome state.

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
