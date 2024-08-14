import random
import itertools
from .fitness import count_one

def roulette_wheel(population: list, select_size: int)->list:
    """ roulette wheel selection """
    assert len(population) != 0, "The size of the population must not be zero"

    selected_population = []
    fitnesses = list(map(count_one, population))
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        raise ValueError("Total fitness is zero. Ensure population has positive fitness values.")
    selection_proba = list(map(lambda x: x/total_fitness, fitnesses))

    for _ in range(select_size):
        cumulative_proba= 0.0
        rand = random.random()
        for idx, p in enumerate(selection_proba):
            cumulative_proba += p
            if rand < cumulative_proba:
                selected_population.append(population[idx])
                break

    return selected_population

def tournament(population: list, select_size: int, size_tournament: int)->list:
    """ random tournament selection """

    selected_population = []

    # size_next_population만큼 tournament 진행
    for _ in range(select_size):
        # 지정한 tournament 사이즈만큼 object를 비복원 추출
        tournament_pop = random.sample(population, k=size_tournament)

        # 적합도가 가장 높은 object 선택
        winner_obj = sorted(tournament_pop, key=count_one)[-1]
        selected_population.append(winner_obj)

    return selected_population

def rank(population: list, select_size: int)->list:
    """ rank selection """
    assert len(population) != 0, "The size of the population must not be zero"

    selected_population = []
    fitnesses = sorted(list(map(count_one, population)), reverse=True)
    selection_proba = [f/len(population) for f in fitnesses]

    for _ in range(select_size):
        cumulative_proba= 0.0
        rand = random.random()
        for idx, p in enumerate(selection_proba):
            cumulative_proba += p
            if rand < cumulative_proba:
                selected_population.append(population[idx])
                break

    return selected_population

if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from population import GeneratePopulate

    x = GeneratePopulate(15).population
    print(x)

    # z = tournament(x, 3, 3)
    # print(z)

    # k = roulette_wheel(x, 100)
    # print(k)

    a = roulette_wheel(x, 100)
    print(a)
