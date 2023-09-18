# **Introduction**

In this kata, your task is to implement an extended version of the famous rock-paper-scissors game. The rules are as follows:

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors

## **Task**:

Given two values from the above game, return the Player result as `"Player 1 Won!"`, `"Player 2 Won!"`, or `"Draw!"`.

## **Inputs**:

Values will be given as one of `"rock", "paper", "scissors", "lizard", "spock"`.

# **Sample Tests**

```python
import codewars_test as test
from solution import rpsls

@test.describe('rock paper scissors lizard spock')
def test():
    @test.it('Player 1 Won!')
    def _():
        test.assert_equals(rpsls('rock', 'lizard'), 'Player 1 Won!')
        test.assert_equals(rpsls('paper', 'rock'), 'Player 1 Won!')
        test.assert_equals(rpsls('scissors', 'lizard'), 'Player 1 Won!')
        test.assert_equals(rpsls('lizard', 'paper'), 'Player 1 Won!')
        test.assert_equals(rpsls('spock', 'rock'), 'Player 1 Won!')
    
    @test.it('Player 2 Won!')
    def _():
        test.assert_equals(rpsls('lizard','scissors'), 'Player 2 Won!')
        test.assert_equals(rpsls('spock','lizard'), 'Player 2 Won!')
        test.assert_equals(rpsls('paper','lizard'), 'Player 2 Won!')
        test.assert_equals(rpsls('scissors','spock'), 'Player 2 Won!')
        test.assert_equals(rpsls('rock','spock'), 'Player 2 Won!')
    
    @test.it("Draw!")
    def _():
        test.assert_equals(rpsls('rock', 'rock'), 'Draw!')
        test.assert_equals(rpsls('spock', 'spock'), 'Draw!')
```

# **Solution**

```python
def rpsls(pl1, pl2):
    rules = {
        "scissors": ["paper", "lizard"],
        "paper": ["rock", "spock"],
        "rock": ["lizard", "scissors"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    if pl1 == pl2:
        return "Draw!"
    return 'Player 1 Won!' if pl2 in rules[pl1] else 'Player 2 Won!'
```