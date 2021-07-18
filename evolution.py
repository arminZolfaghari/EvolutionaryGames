import copy
import random

from player import Player
import numpy as np
from config import CONFIG

mutation_prob = 0.3


# plot average, max, min of fitness function
def plotting():
    pass


# add noise to matrix for mutation
def add_noise(matrix):
    # noise = np.random.uniform(-0.5, 0.5, matrix.shape)
    matrix_copy = copy.deepcopy(matrix)
    noise = np.random.normal(0, 0.5, matrix.shape)
    matrix_copy += noise
    return matrix_copy


# get fitness all players
def get_players_fitness(players):
    players_fitness = []
    for player in players:
        players_fitness.append(player.fitness)
    return players_fitness


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):
        # TODO
        # child: an object of class `Player`
        child.nn.W1 = add_noise(child.nn.W1)
        child.nn.b1 = add_noise(child.nn.b1)
        child.nn.W2 = add_noise(child.nn.W2)
        child.nn.b2 = add_noise(child.nn.b2)

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            prev_players_copy = copy.deepcopy(prev_players)

            players_fitness_arr = get_players_fitness(prev_players_copy)
            prev_players_copy.sort(key=lambda x: x.fitness, reverse=True)

            # create child from best parent
            children_arr = []
            for i in range(num_players):
                # parent = random.choices(prev_players, weights=players_fitness_arr, k=1)
                child = prev_players_copy[i]
                # if random.random() < mutation_prob:
                self.mutate(child)
                children_arr.append(child)

        # new_players = children_arr + prev_players
        # new_players.sort(key=lambda x: x.fitness, reverse=True)
        return children_arr


    def next_population_selection(self, players, num_players):
        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        players.sort(key=lambda x: x.fitness, reverse=True)
        plotting()
        # for player in players:
        #     print(player.fitness)
        return players[: num_players]
