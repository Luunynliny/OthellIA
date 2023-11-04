import numpy as np

from genetic.crossover import (
    one_point_crossover,
    two_point_crossover,
    uniform_crossover,
)


def test_one_point_crossover(monkeypatch):
    values = [3, 5, 1]
    i = 0

    class Mock_default_rng:
        def integers(self, a, b):
            nonlocal i
            i += 1
            return values[i - 1]

    monkeypatch.setattr(np.random, "default_rng", Mock_default_rng)

    p1 = np.array([1, 1, 1, 1, 1, 1])
    p2 = np.array([0, 0, 0, 0, 0, 0])

    assert np.allclose(
        one_point_crossover(p1, p2),
        (
            np.array([0, 0, 0, 0.33, 0.33, 0.33]),
            np.array([0.33, 0.33, 0.33, 0, 0, 0]),
        ),
        atol=1e-2,
    )

    assert np.allclose(
        one_point_crossover(p1, p2),
        (
            np.array([0, 0, 0, 0, 0, 1]),
            np.array([0.2, 0.2, 0.2, 0.2, 0.2, 0]),
        ),
        atol=1e-2,
    )

    assert np.allclose(
        one_point_crossover(p1, p2),
        (
            np.array([0, 0.2, 0.2, 0.2, 0.2, 0.2]),
            np.array([1, 0, 0, 0, 0, 0]),
        ),
        atol=1e-2,
    )


def test_two_point_crossover(monkeypatch):
    values = np.array([[2, 3], [2, 4], [1, 2]])
    i = 0

    class Mock_default_rng:
        def choice(self, a, b, replace):
            nonlocal i
            i += 1
            return values[i - 1]

    monkeypatch.setattr(np.random, "default_rng", Mock_default_rng)

    p1 = np.array([1, 1, 1, 1, 1, 1])
    p2 = np.array([0, 0, 0, 0, 0, 0])

    assert np.allclose(
        two_point_crossover(p1, p2),
        (
            np.array([0.2, 0.2, 0, 0.2, 0.2, 0.2]),
            np.array([0, 0, 1, 0, 0, 0]),
        ),
        atol=1e-2,
    )

    assert np.allclose(
        two_point_crossover(p1, p2),
        (
            np.array([0.25, 0.25, 0, 0, 0.25, 0.25]),
            np.array([0, 0, 0.5, 0.5, 0, 0]),
        ),
        atol=1e-2,
    )

    assert np.allclose(
        two_point_crossover(p1, p2),
        (
            np.array([0.2, 0, 0.2, 0.2, 0.2, 0.2]),
            np.array([0, 1, 0, 0, 0, 0]),
        ),
        atol=1e-2,
    )


def test_uniform_crossover(monkeypatch):
    values = np.array(
        [[1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
    )
    i = 0

    class Mock_default_rng:
        def choice(self, a, size, p):
            nonlocal i
            i += 1
            return values[i - 1]

    monkeypatch.setattr(np.random, "default_rng", Mock_default_rng)

    p1 = np.array([1, 1, 1, 1, 1, 1])
    p2 = np.array([0, 0, 0, 0, 0, 0])

    assert np.allclose(
        uniform_crossover(p1, p2, 0.5),
        (
            np.array([0, 0, 0.5, 0.5, 0, 0]),
            np.array([0.25, 0.25, 0, 0, 0.25, 0.25]),
        ),
        atol=1e-2,
    )

    assert np.allclose(
        uniform_crossover(p1, p2, 0.8),
        (
            np.array([0, 0, 0, 0, 0.5, 0.5]),
            np.array([0.25, 0.25, 0.25, 0.25, 0, 0]),
        ),
        atol=1e-2,
    )

    assert np.allclose(
        uniform_crossover(p1, p2, 0.1),
        (
            np.array([0.2, 0.2, 0.2, 0, 0.2, 0.2]),
            np.array([0, 0, 0, 1, 0, 0]),
        ),
        atol=1e-2,
    )
