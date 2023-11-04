import numpy as np

from genetic.crossover import one_point_crossover


def test_one_point_crossover(monkeypatch):
    values = [3, 5, 1]
    i = 0

    class Mock_default_rng:
        def integers(self, a, b):
            nonlocal i
            i += 1
            return values[i - 1]

    monkeypatch.setattr(np.random, "default_rng", Mock_default_rng)

    p1 = [1, 1, 1, 1, 1, 1]
    p2 = [2, 2, 2, 2, 2, 2]

    assert np.array_equal(
        one_point_crossover(p1, p2),
        (np.array([2, 2, 2, 1, 1, 1]), np.array([1, 1, 1, 2, 2, 2])),
    )

    assert np.array_equal(
        one_point_crossover(p1, p2),
        (np.array([2, 2, 2, 2, 2, 1]), np.array([1, 1, 1, 1, 1, 2])),
    )

    assert np.array_equal(
        one_point_crossover(p1, p2),
        (np.array([2, 1, 1, 1, 1, 1]), np.array([1, 2, 2, 2, 2, 2])),
    )
