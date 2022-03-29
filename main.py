from audioop import reverse
from pickle import TRUE
import random
import numpy as np

max_r = 5
min_r = -5


def convert(list):
    # res = int("".join(map(str, list)))
    conv = 0
    for i in range(3):
        conv += list[i] * (10 ** (-(i + 1)))
    return conv


def encode(genotype):
    converted = convert(genotype)
    # phenotype = (converted * (max_r - min_r) / 999) - min_r
    phenotype = (min_r + ((max_r - min_r) / 9 * 0.111) + converted)
    return phenotype


def heuristic(x, y):
    return ((np.sin(x) + np.cos(y)) ** 2) / x ** 2 + y ** 2


def fitness(x, y):
    return 1/heuristic(x, y) + (10 ** -20)


def define_individual(individual):
    individual["phenotype-x"] = encode(list(individual["genotype"][:3]))
    individual["phenotype-y"] = encode(list(individual["genotype"][3:]))
    individual["heuristic"] = heuristic(
        individual["phenotype-x"], individual["phenotype-y"])


def generate_population(population):
    individual = {}
    individual["genotype"] = random.choices(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=6)
    define_individual(individual)
    population.append(individual)


def check(s, p):
    check = False
    for i in p:
        if i == s:
            check = True
            return check

    return check


def parent_selection(population):
    parents = []
    fitnesses = list(map(lambda x: fitness(
        x["phenotype-x"], x["phenotype-y"]), population))
    weight = list(fitnesses[i] / sum(fitnesses)
                  for i in range(len(fitnesses)))
    while len(parents) < 2:
        select = random.choices(population, weights=weight)[0]
        if not check(select, parents):
            parents.append(select)
    return parents


def crossover(population, parent1, parent2):
    cross = random.randint(1, len(parent1["genotype"]) - 2)
    child1 = {}
    child2 = {}

    child1["genotype"] = parent1["genotype"][:cross] + \
        parent2["genotype"][cross:]
    child2["genotype"] = parent2["genotype"][:cross] + \
        parent1["genotype"][cross:]

    # child1 = {"genotype": [parent1["genotype"]
    #                        [:cross] + parent2["genotype"][cross:]]}
    # child2 = {"genotype": [parent2["genotype"]
    #                        [:cross] + parent1["genotype"][cross:]]}

    chance = random.random()
    if chance <= 0.05:
        mutate = random.randint(0, len(child1["genotype"]) - 1)
        change = random.randint(0, 9)
        child1["genotype"][mutate] = change

    chance = random.random()
    if chance <= 0.05:
        mutate = random.randint(0, len(child2["genotype"]) - 1)
        change = random.randint(0, 9)
        child2["genotype"][mutate] = change

    define_individual(child1)
    define_individual(child2)

    population.append(child1)
    population.append(child2)


def survivor_selection(population):
    population.sort(key=lambda x: x["heuristic"], reverse=True)
    while len(population) > 20:
        population.pop()


population = []
for i in range(20):
    generate_population(population)

# for j in population:
#     print(j)


for j in range(1, 61, 1):
    parents = parent_selection(population)
    crossover(population, parents[0], parents[1])
    survivor_selection(population)
    print(f"Generation {j} : ", fitness(
        population[0]["phenotype-x"], population[0]["phenotype-y"]))
    print(
        f"x = {encode(list(population[0]['genotype'][:3]))}, y = {encode(list(population[0]['genotype'][3:]))}")
