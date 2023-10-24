import pytest

from genetic.population import (
    generate_random_chromosome,
    generate_random_population,
)


def test_generate_random_chromosome():
    chromosome = generate_random_chromosome()

    assert len(chromosome) == 6
    assert sum(chromosome) == pytest.approx(1)


def test_generate_random_population():
    size = 10
    population = generate_random_population(size)

    assert population.shape == (size, 6)
    assert population.sum().sum() == pytest.approx(size)
