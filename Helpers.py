def get_prob_winning(results):
    wins = 0
    for result in results:
        ending, game_state = result
        wins += ending
    return wins / len(results)
