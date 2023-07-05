# **Instructions**

Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

**Examples**

```js
2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
```

# **Sample Tests**

```js
describe('summation', function () {
  it('should return the correct total', function () {
    assert.strictEqual(summation(1),  1);
    assert.strictEqual(summation(2),  3);
    assert.strictEqual(summation(8), 36);
  })
})
```

# **Solution**

```js
const summation = (num) => {
	let sum = 0;
	for (let i = 1; i <= num; i++) {
		sum += i;
	}
	return sum;
}
```