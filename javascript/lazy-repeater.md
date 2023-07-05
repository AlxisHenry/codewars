# **Instructions**

The makeLooper() function (or make_looper in your language) takes a string (of non-zero length) as an argument. It returns a function. The function it returns will return successive characters of the string on successive invocations. It will start back at the beginning of the string once it reaches the end.

**Examples**

```js
var abc = makeLooper('abc');
abc(); // should return 'a' on this first call
abc(); // should return 'b' on this second call
abc(); // should return 'c' on this third call
abc(); // should return 'a' again on this fourth call
```

# **Sample Tests**

```js
describe("Sample Tests", function() {
  const abc = makeLooper("abc");
  it("Should cycle through the given string", function() {
    assert.strictEqual(abc(), "a")
    assert.strictEqual(abc(), "b")
    assert.strictEqual(abc(), "c")
  });
  it("Should return to its initial cycle once it reaches the end", () => {
    assert.strictEqual(abc(), "a")
    assert.strictEqual(abc(), "b")
    assert.strictEqual(abc(), "c")
  })
});
```

# **Solution**

```js
function makeLooper(str) {
	let i = 0;
	return () => {
		if (i === str.length) i = 0;
		return str[i++];
	}
}
``` 