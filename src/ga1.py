# generation을 지정하는 경우

from tqdm import tqdm
from util.method.fitness import count_one
from util.population import GeneratePopulate
from util.operator import select, crossover, mutate, replace

def main():
    """
    select method : roulette_wheel, tournament (size_tournament), rank
    replace method : all, elitism (elite_rate), steady_state
    """
    generations = 50
    chromo_size = 30
    population_size = 10000
    mut_rate = 0.7
    tournament_size = 10 # if need
    elite_rate = 0.01 # if need

    pop_inst = GeneratePopulate(chromo_size)
    population = pop_inst.rand_pop_generate(population_size)
    select_size = int(pop_inst.size()*1)

    for gen in range(generations):
        parents = select(population, select_size, "tournament", size_tournament = tournament_size)
        childs = crossover(parents)
        childs = mutate(childs, mut_rate)
        population = replace(population, childs, "elitism", elite_rate = elite_rate) #elite_rate
        fitness_dict = {count_one(object):object for object in population}
        max_fitness = max(fitness_dict)

        print(f"Generation {gen+1}: Best Fitness = {max_fitness}, Object = {fitness_dict[max_fitness]}")


if __name__ == '__main__':
    main()