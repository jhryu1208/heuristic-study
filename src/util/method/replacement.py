import logging
from .fitness import count_one
""" replace 이후/이전 population 크기는 동일해야함을 반드시 지키도록 가정 """

def generation_repl(parent_population:list, child_population: list)->list:
    """ 전세대 교체 """

    assert len(parent_population) == len(child_population), "the size of child population must be equal to the size of parent population"
    next_population = child_population
    return next_population

def elitism_repl(parent_population:list, child_population: list, elite_rate:float = 0.0)->list:
    """ elitism : 얼마나 최상위 부모를 남길 것인가 """

    parent_size, child_size = len(parent_population), len(child_population)
    min_elite_rate = (parent_size-child_size)/parent_size
    logging.info(f"Input parent population size : {parent_size}")
    logging.info(f"Input child population size : {child_size}")

    assert (elite_rate >= 0.0) & (elite_rate <= 1.0), "the elite_rate must be between 0 and 1"
    # 부모수가 자식수보다 적다는 것은, 자식의 다양성이 좋지 않다는 것을 의미하니깐 해당 경우는 제외
    assert parent_size >= child_size, "For diversity, the size of parent population should be larger than the size of child population"
    # child population 사이즈가 너무 작을 경우, 뽑는 부모 객체의 수를 늘려 기존 Population 사이즈를 유지한다.
    assert elite_rate >= min_elite_rate, f"elite_rate must be higher than {min_elite_rate}"

    sorted_parents = sorted(parent_population, key=count_one, reverse=True) # fitness 기준으로 내림차순
    sorted_childs = sorted(child_population, key=count_one, reverse=True) # fitness 기준으로 내림차순

    elite_parents = sorted_parents[:int(parent_size*elite_rate)]
    replace_size = parent_size - len(elite_parents)
    replace_childs = sorted_childs[:replace_size]

    next_population = elite_parents + replace_childs

    return next_population

def steady_state_repl(parent_population:list, child_population: list): # 약간 아리송...
    """ Steady State Replacement : 부모와 자식의 Population 을 병합 및 정렬하고, 다시 부모 population size만큼 슬라이싱 """

    parent_size, child_size = len(parent_population), len(child_population)

    logging.info(f"Input parent population size : {parent_size}")
    logging.info(f"Input child population size : {child_size}")
    # 부모수가 자식수보다 적다는 것은, 자식의 다양성이 좋지 않다는 것을 의미하니깐 해당 경우는 제외
    assert parent_size >= child_size, "For diversity, the size of parent population should be larger than the size of child population"

    sorted_combined_population = sorted(parent_population + child_population, key = count_one, reverse=True)
    next_population = sorted_combined_population[:parent_size]

    return next_population

def partial_repl(parent_population:list, child_population: list, method_name: str, repl_rate:float = 0.0)->list:
    """ Partial Replacement """

    pass


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from population import GeneratePopulate

    x = GeneratePopulate(10).population
    y = x
    e = 0.001
    z = elitism_repl(x, y, e)
    print(len(z))