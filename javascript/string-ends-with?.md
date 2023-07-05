# **Instructions**

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

**Examples**

```js
solution('abc', 'bc') // returns true
solution('abc', 'd') // returns false
```

# **Sample Tests**

```js
describe("Tests", () => {
  it("test", () => {
		Test.assertEquals(solution('abcde', 'cde'), true)
		Test.assertEquals(solution('abcde', 'abc'), false)
	});
});

```

# **Solution**

```js
const solution = (str, ending) => str.slice(str.length - ending.length) === ending;
```

*More optimized solution:*

```js
const solution = (str, ending) => str.endsWith(ending);
```