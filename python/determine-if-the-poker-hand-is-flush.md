# **Introduction**

Determine if the poker hand is flush, meaning if the five cards are of the same suit.

Your function will be passed a list/array of 5 strings, each representing a poker card in the format `"5H"` (5 of hearts), meaning the value of the card followed by the initial of its suit (`H`earts, `S`pades, `D`iamonds or `C`lubs). No jokers included.

Your function should return `true` if the hand is a flush, `false` otherwise.

The possible card values are `2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A`

## **Examples**

```python
["AS", "3S", "9S", "KS", "4S"]  ==> True
["AD", "4S", "7H", "KS", "10S"] ==> False
```

# **Sample Tests**

```js
test.assert_equals(is_flush(["AS", "3S", "9S", "KS", "4S"]), True)
test.assert_equals(is_flush(["AD", "4S", "7H", "KC", "5S"]), False)
test.assert_equals(is_flush(["AD", "4S", "10H", "KC", "5S"]), False)
test.assert_equals(is_flush(["QD", "4D", "10D", "KD", "5D"]), True)
```

# **Solution**

```python
def is_flush(cards):
	colors = []
	for k, card in enumerate(cards):
		colors.append(card[-1])
	return all(x == colors[0] for x in colors)
```

```python
def is_flush(cards):
	for card in cards:
		if card[-1] != cards[0][-1]:
			return False
	return True
```