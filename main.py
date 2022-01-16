import multiprocessing as mp
from ObstgartenGame import ObstgartenGame, simulate
from Helpers import get_prob_winning

# Params:
num_simulations = 100000
num_fruits_taken_if_dice_shows_basket = 1

# Run simulations:
print(f'num_simulations: {num_simulations}\n'
      f'num_fruits_taken_if_dice_shows_basket: {num_fruits_taken_if_dice_shows_basket}\n'
      f'{52 * "-"}')
for strategy in ['max', 'min', 'random']:
    obstgarten_games = [ObstgartenGame(strategy, num_fruits_taken_if_dice_shows_basket) for i in range(num_simulations)]
    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = pool.map(simulate, obstgarten_games)
    prob_winning = get_prob_winning(results)
    print(f'strategy: {strategy}{(15 - len(strategy)) * " "}probability_winning: {100 * prob_winning:.2f}%')
