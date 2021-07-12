import copy
import random

from player import Player
import numpy as np
from config import CONFIG

mutation_prob = 0.4


# add noise to matrix for mutation
def add_noise(matrix):
    noise = np.random.normal(0, 0.2, matrix.shape)
    matrix += noise
    return matrix


# get fitness all players
def get_players_fitness(players):
    players_fitness = []
    for player in players:
        players_fitness.append(player.fitness)


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


            players_fitness_arr = get_players_fitness(prev_players)

            # create child from best parent
            children_arr = []
            for i in range(num_players):
                # parent = random.choices(prev_players, weights=players_fitness_arr, k=1)
                parent = prev_players[i]
                child = copy.deepcopy(parent)
                # if random.random() < mutation_prob:
                self.mutate(child)
                children_arr.append(child)


            new_players = prev_players + children_arr
            new_players.sort(key=lambda x: x.fitness, reverse=True)
            return new_players[: num_players]

    def next_population_selection(self, players, num_players):

        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        players.sort(key=lambda x: x.fitness, reverse=True)
        # for player in players:
        #     print(player.fitness)

        return players[: num_players]
