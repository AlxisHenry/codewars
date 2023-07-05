# **Instructions**

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9.

```js
[1, 2, 2] => 1**2 + 2**2 + 2**2 = 9
```

# **Sample Tests**

```js
describe("Tests", () => {
  it("test", () => {
    assert.strictEqual(squareSum([1,2]), 5);
    assert.strictEqual(squareSum([0, 3, 4, 5]), 50);
    assert.strictEqual(squareSum([]), 0);
  });
});
```

# **Solution**

```js
const squareSum = (numbers) => numbers.reduce((sum, n) => sum + (n * n), 0);
```