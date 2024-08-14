import random
import numpy as np
from .method.selection import roulette_wheel, tournament, rank
from .method.replacement import generation_repl, elitism_repl, steady_state_repl

""" 현 문제에서는 함수로 operator를 구성하는게 적당할 것 같다."""

def select(population:list, select_size: int, method_name, **kwargs)->list:
    """ input된 method_name으로 select과정 진행 """
    assert len(population) >= select_size, "select object size must be less than the size of the original population"

    method = {
        "roulette": roulette_wheel,
        "tournament": tournament,
        "rank": rank,
    }
    select_population = method.get(method_name, "roulette")(population, select_size, **kwargs)

    return select_population # = parent_population

def crossover(selected_population: list)->list:
    """
    무작위 추출로 부모를 선택하고, 교차변이를 통해 자식 생성
    생성 자식 수 = 후보 부모 수(# of population)
    """
    crossover_population = []
    size = len(selected_population)

    for _ in range(0, size):
        p1 = random.choice(selected_population)
        p2 = random.choice(selected_population)
        cross_point = random.randint(0, selected_population[0].shape[0]-1)
        c = np.concatenate((p1[:cross_point], p2[cross_point:]))
        crossover_population.append(c)

    return crossover_population

def mutate(crossover_population:list, mut_rate: float)->list:
    """
    각 객체내 유전자들이 mut_rate 확률로 변이됨
    """
    mutate_population = []

    for object in crossover_population:
        for i in range(len(object)):
            if random.random() < mut_rate:
                object[i] = not bool(object[i])

        mutate_population.append(object)

    return mutate_population

def replace(parent_population:list, child_population: list, method_name, **kwargs)->list:
    """
    부모 개체군의 크기를 유지하면서 새로운 자손으로 일부 또는 전체 개체를 교체
    """

    method = {
        "all": generation_repl,
        "elitism": elitism_repl,
        "steady_state": steady_state_repl,
    }

    replace_population = method.get(method_name, "roulette")(parent_population, child_population, **kwargs)

    return replace_population


if __name__ == '__main__':
    import sys
    import os
    from population import GeneratePopulate

    origin_population = GeneratePopulate(5).population
    print(origin_population)
    # next_population = crossover(origin_population)
    # next_population = mutate(origin_population, 0.45)
    #
    # print(next_population)
    # print(len(next_population))

    ex1 = select(origin_population, 20,  "roulette")
    ex2 = select(origin_population, 20, "tournament", size_tournament=5)
    ex3 = select(origin_population, 20, "rank")
    print(f"""
    [select result]
    - original population(size: {len(origin_population)}) : {origin_population}
    - roulette(size: {len(ex1)}) : {ex1}
    - tournament(size: {len(ex2)}) : {ex2}
    - rank(size: {len(ex3)}) : {ex3}
    """)

