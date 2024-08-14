# Best를 찾을 때 까지 탐색

from tqdm import tqdm
from util.method.fitness import count_one
from util.population import GeneratePopulate
from util.operator import select, crossover, mutate, replace

def main():
    """
    select method : roulette_wheel, tournament (size_tournament), rank
    replace method : all, elitism (elite_rate), steady_state
    """
    chromo_size = 100
    population_size = 10000
    mut_rate = 0.5
    tournament_size = 15 # if need
    elite_rate = 0.1 # if need

    pop_inst = GeneratePopulate(chromo_size)
    population = pop_inst.rand_pop_generate(population_size)
    select_size = int(pop_inst.size()*1)

    is_found = False
    gen = 0

    while not is_found:
        gen += 1

        parents = select(population, select_size, "tournament", size_tournament = tournament_size)
        childs = crossover(parents)
        childs = mutate(childs, mut_rate)
        population = replace(population, childs, "elitism", elite_rate = elite_rate) #elite_rate
        fitness_dict = {count_one(object):object for object in population}
        max_fitness = max(fitness_dict)

        if max_fitness == chromo_size:
            is_found = True
            print('Target found')
            print(f"Generation {gen+1}: Best Fitness = {max_fitness}, Object = {fitness_dict[max_fitness]}")
        else:
            print(f"Generation {gen+1}: Best Fitness = {max_fitness}, Object = {fitness_dict[max_fitness]}")


if __name__ == '__main__':
    main()