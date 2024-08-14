import random

# 초기 인구 생성
def generate_initial_population(pop_size, gene_length):
    return [[random.randint(0, 1) for _ in range(gene_length)] for _ in range(pop_size)]

# 적합도 평가 함수 (예: 1의 개수를 적합도로 간주)
def evaluate_fitness(individual):
    return sum(individual)

# 선택 함수 (예: 토너먼트 선택)
def select_parents(population, fitnesses, tournament_size=3):
    parents = []
    for _ in range(2):
        tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
        parents.append(max(tournament, key=lambda x: x[1])[0])
    return parents

# 교차 및 돌연변이 함수
def crossover_and_mutate(parent1, parent2, mutation_rate=0.01):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    for child in [child1, child2]:
        for i in range(len(child)):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]
    return child1, child2

# Partial Replacement 함수
def partial_replacement(population, fitnesses, children, replacement_rate=0.2):
    num_replacements = int(len(population) * replacement_rate)
    replacement_indices = random.sample(range(len(population)), num_replacements)

    for i in range(num_replacements):
        replacement_index = replacement_indices[i]
        population[replacement_index] = children[i % len(children)]
        fitnesses[replacement_index] = evaluate_fitness(children[i % len(children)])

    return population, fitnesses

if __name__ == '__main__':
    # 메인 알고리즘
    pop_size = 10
    gene_length = 5
    generations = 20
    replacement_rate = 0.2

    population = generate_initial_population(pop_size, gene_length)
    fitnesses = [evaluate_fitness(ind) for ind in population]


    for gen in range(generations):
        parent1, parent2 = select_parents(population, fitnesses)
        child1, child2 = crossover_and_mutate(parent1, parent2)

        population, fitnesses = partial_replacement(population, fitnesses, [child1, child2], replacement_rate)

        print(f"Generation {gen+1}: Best Fitness = {max(fitnesses)}")

    # 최종 결과
    best_individual = max(zip(population, fitnesses), key=lambda x: x[1])[0]
    print("Best Individual:", best_individual)
    print("Best Fitness:", evaluate_fitness(best_individual))
