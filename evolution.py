import copy
import random

from player import Player
import numpy as np
from config import CONFIG
from SaveGeneration import *

mutation_prob = 0.3


def generate_random_uniform():
    return np.random.uniform(0, 1, 1)[0]


# save generation information
def save_generation_information(max, min, avg):
    write_to_file(max, min, avg)


# add noise to matrix for mutation
def add_noise(matrix, noise):
    # noise = np.random.uniform(-0.5, 0.5, matrix.shape)
    matrix_copy = copy.deepcopy(matrix)
    noise = np.random.normal(0, noise, matrix.shape)
    matrix_copy += noise
    return matrix_copy


# get fitness all players
def get_players_fitness(players):
    players_fitness = []
    for player in players:
        players_fitness.append(player.fitness)
    return players_fitness


def new_fitness_function(fitness_arr):
    new_fitness_arr = []
    for fitness in fitness_arr:
        new_fitness_arr.append(fitness ** 2)

    return new_fitness_arr


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):
        # child: an object of class `Player`
        if generate_random_uniform() <= mutation_prob:
            child.nn.W1 = add_noise(child.nn.W1, 0.5)
        if generate_random_uniform() <= mutation_prob:
            child.nn.b1 = add_noise(child.nn.b1, 0.5)
        if generate_random_uniform() <= mutation_prob:
            child.nn.W2 = add_noise(child.nn.W2, 0.5)
        if generate_random_uniform() <= mutation_prob:
            child.nn.b2 = add_noise(child.nn.b2, 0.5)

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`

            prev_players_copy = copy.deepcopy(prev_players)
            players_fitness_arr = get_players_fitness(prev_players_copy)
            players_new_fitness_arr = new_fitness_function(players_fitness_arr)
            # prev_players_copy.sort(key=lambda x: x.fitness, reverse=True)

            # create child from best parent
            children_arr = []

            parent = random.choices(prev_players_copy, weights=players_new_fitness_arr, k=150)
            for i in range(num_players):
                # parent = random.choices(prev_players, weights=players_fitness_arr, k=1)
                child = copy.deepcopy(parent[i])
                # if random.random() < mutation_prob:
                self.mutate(child)
                children_arr.append(child)

            # while len(children_arr) > num_players:
            #     parents = random.choices(prev_players_copy, weights=[1] * num_players, k=2)
            #     parent1 = copy.deepcopy(parents[0])
            #     parent2 = copy.deepcopy(parents[1])
            #     child.nn.W1, child.nn.W2, child.nn.b1, child.nn.b2 = self.crossover(parent1, parent2)

        return children_arr

    def crossover(self, parent1, parent2):
        child_w1 = parent1.nn.W1 + parent2.nn.W1
        child_w2 = parent1.nn.W2 + parent2.nn.W2
        child_b1 = parent1.nn.b1 + parent2.nn.b1
        child_b2 = parent1.nn.b2 + parent2.nn.b2

        return child_w1, child_w2, child_b1, child_b2

    def next_population_selection(self, players, num_players):
        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        # TODO (additional): a selection method other than `top-k`

        # save generation information to plotting
        all_fitness_in_generation = get_players_fitness(players)
        max = np.max(all_fitness_in_generation)
        min = np.min(all_fitness_in_generation)
        avg = np.mean(all_fitness_in_generation)
        save_generation_information(max, min, avg)

        players.sort(key=lambda x: x.fitness, reverse=True)
        # for player in players:
        #     print(player.fitness)
        return players[: num_players]
