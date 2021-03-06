import random

import numpy as np


class ObstgartenGame:
    def __init__(self, strategy, num_fruits_taken_if_dice_shows_basket=1, num_each_fruit=4, num_raven_winning=5):
        self.strategy = strategy
        self.num_fruits_taken_if_dice_shows_basket = num_fruits_taken_if_dice_shows_basket
        self.fruits = np.array([num_each_fruit, num_each_fruit, num_each_fruit, num_each_fruit], dtype=np.int)
        self.num_raven_winning = num_raven_winning
        self.raven = 0


def simulate(game):
    while game.raven < game.num_raven_winning and np.sum(game.fruits) != 0:
        dice = random.randint(0, 5)  # 0-3 idx fruit, 4 raven, 5 basket
        if dice < 4:
            update_fruits(game, dice)
        elif dice == 4:
            game.raven += 1
        else:
            for i in range(game.num_fruits_taken_if_dice_shows_basket):
                if np.sum(game.fruits) == 0:
                    continue
                update_fruits(game)
    assert (game.raven == game.num_raven_winning and np.sum(game.fruits) != 0) or \
           (game.raven < game.num_raven_winning and np.sum(game.fruits) == 0)
    if game.raven == game.num_raven_winning:
        return 0, [game.raven, game.fruits]
    return 1, [game.raven, game.fruits]


def update_fruits(game, idx=None):
    if idx is None:
        if game.strategy == 'max':
            idx = np.argmax(game.fruits)
        elif game.strategy == 'min':
            idx = np.where(game.fruits == np.min(game.fruits[game.fruits != 0]))[0][0]
        elif game.strategy == 'random':
            non_zero_idxs = np.argwhere(game.fruits != 0).reshape(-1)
            idx = non_zero_idxs[random.randint(0, len(non_zero_idxs) - 1)]
        else:
            print('strategy not recognized, defaulting to max strategy ... ')
            idx = np.argmax(game.fruits)
    game.fruits[idx] = np.maximum(0, game.fruits[idx] - 1)
