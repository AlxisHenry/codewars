# **Instructions**

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

**Examples**

```js
undefined
```

# **Sample Tests**

```js
describe("Vowels Count Tests",function(){
  it("should return 5 for 'abracadabra'",function(){
    assert.strictEqual(getCount("abracadabra"), 5) ;
  });
});
```

# **Solution**

```js
function getCount(str, count = 0) {
  for (const letter of str.split('')) {
    if (["a", "e", "i", "o", "u"].includes(letter)) count++;
  }
  return count;
}
```