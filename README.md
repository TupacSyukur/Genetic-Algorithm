# Genetic-Algorithm
## Purpose
This code is an assignment for Introduction to Artificial Intelligence class.
## Algorithm
We create genetic algorithm from scratch, which means that we're only using standard library and not specifically library for genetic algorithm. We're using numpy and random library to count fitness function. For representation, we're using 6 digits of integer, because it helps when it comes to float/real number. In the parent selection, we're using roulette wheel selection to select two parents that we're going to use when crossover and mutation. For crossover we're only slice the individual in one point. For mutation, we're only do it if the probability is below 5% and we're gonna randomized the position and the number. Lastly, the survivor selection will filter out the small heuristic value and let the bigger heuristic value.
