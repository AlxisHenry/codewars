# **Introduction**

You spent all your saved money to buy some shares.

You bought it for invested, and want to know how much it's worth, but all the info you can quickly get are just the change the shares price made in percentages.

Your task:
Write the function sharePrice() that calculates, and returns the current price of your share, given the following two arguments:

invested(number), the amount of money you initially invested in the given share

changes(array of numbers), contains your shares daily movement percentages

The returned number, should be in string format, and it's precision should be fixed at 2 decimal numbers.

Have fun!

Hint: Try to write the function in a functional manner!

# **Sample Tests**

```python
test.assert_equals(share_price(100, []), '100.00')
test.assert_equals(share_price(100, [-50, 50]), '75.00')
test.assert_equals(share_price(100, [-50, 100]), '100.00')
test.assert_equals(share_price(100, [-20, 30]), '104.00')
test.assert_equals(share_price(1000, [0, 2, 3, 6]), '1113.64')
```

# **Solution**

```python
def share_price(invested, changes):
    currentPrice = invested
    for c in changes:
        currentPrice *= (1 + c/100)
    return str("{:.2f}".format(currentPrice))
```