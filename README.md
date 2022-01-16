# mein_erster_obstgarten_monte_carlo

## Description

This is a fun project looking at Monte Carlo simulation of the children board
game ["Mein erster Obstgarten"](https://www.haba-play.com/de_DE/meine-ersten-spiele-erster-obstgarten--003177).

## Results

Results after 100000 simulations for varying player strategies _min, max, random_ and _number of fruits taken if the
dice showed the basket symbol_

```commandline
num_simulations: 100000
num_fruits_taken_if_dice_shows_basket: 1
----------------------------------------------------
strategy: max            probability_winning: 63.32%
strategy: min            probability_winning: 64.64%
strategy: random         probability_winning: 59.61%
```

```commandline
num_simulations: 100000
num_fruits_taken_if_dice_shows_basket: 2
----------------------------------------------------
strategy: max            probability_winning: 76.42%
strategy: min            probability_winning: 80.77%
strategy: random         probability_winning: 74.33%
```

## License

This project is published under the [MIT License](LICENSE.md)