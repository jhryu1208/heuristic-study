import random
import numpy as np
import itertools
class GeneratePopulate():
    """ 지정된 size에 따른 Population 생성 """
    def __init__(self, chromo_size):
        self.chromo_size = chromo_size
        self.population = []

    def pop_generate(self):

        for combination in itertools.product([0, 1], repeat=self.chromo_size):
            self.population.append(np.array(combination))

        return self.population

    def rand_pop_generate(self, pop_size):
        for _ in range(pop_size):
            self.population.append(np.array([random.randint(0, 1) for _ in range(self.chromo_size)]))

        return self.population

    def size(self):
        return len(self.population)

    def rand_select(self):
        """ population 사이즈가 너무 클 경우, 비복원 추출 """
        pass

if __name__=='__main__':
    x = GeneratePopulate(5).population
    print(x)
    print(len(x))
