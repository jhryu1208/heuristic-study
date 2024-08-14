import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.util.population import GeneratePopulate

@pytest.fixture
def gen_population():
    population = GeneratePopulate(3).population
    return population

import random

def roulette_wheel_selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    relative_fitness = [f / total_fitness for f in fitness_scores]
    cumulative_probability = [sum(relative_fitness[:i+1]) for i in range(len(relative_fitness))]

    rand = random.random()
    for i, cp in enumerate(cumulative_probability):
        if rand <= cp:
            return population[i]