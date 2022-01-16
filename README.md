# mein_erster_obstgarten_monte_carlo

## Description

This is a fun project looking at Monte Carlo simulation of the children board
game ["Mein erster Obstgarten"](https://www.haba-play.com/de_DE/meine-ersten-spiele-erster-obstgarten--003177).

## Results

Results after 100000 simulations for varying 
* player strategies (when dice shows basket symbol)
  * _max_: take the fruit that is still the most available
  * _min_: take fruit of which there is the least there
  * _random_: take random available fruit
* number of fruits taken if the dice showed the basket symbol
* numbers of each fruit
* number of steps which the raven needs in order to win

```commandline
num_simulations: 100000
num_fruits: 4
num_raven_winning: 5
num_fruits_taken_if_dice_shows_basket: 1
----------------------------------------------------
strategy: max            probability_winning: 63.16%
strategy: min            probability_winning: 55.69%
strategy: random         probability_winning: 59.95%
```

```commandline
num_simulations: 100000
num_fruits: 4
num_raven_winning: 5
num_fruits_taken_if_dice_shows_basket: 2
----------------------------------------------------
strategy: max            probability_winning: 76.76%
strategy: min            probability_winning: 70.18%
strategy: random         probability_winning: 74.20%
```

```commandline
num_simulations: 100000
num_fruits: 10
num_raven_winning: 9
num_fruits_taken_if_dice_shows_basket: 1
----------------------------------------------------
strategy: max            probability_winning: 47.23%
strategy: min            probability_winning: 32.35%
strategy: random         probability_winning: 40.83%
```

```commandline
num_simulations: 100000
num_fruits: 10
num_raven_winning: 9
num_fruits_taken_if_dice_shows_basket: 2
----------------------------------------------------
strategy: max            probability_winning: 68.56%
strategy: min            probability_winning: 53.72%
strategy: random         probability_winning: 63.35%
```

## License

This project is published under the [MIT License](LICENSE.md)