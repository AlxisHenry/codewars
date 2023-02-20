# **Instructions**

In this example you have to validate if a user input string is alphanumeric. The given string is not ``nil/null/NULL/None``, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character (``""`` is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from ``0`` to ``9``
No whitespaces / underscore

# **Sample Tests**

```js
describe("Tests", () => {
  it("test", () => {
	Test.assertEquals(alphanumeric("Mazinkaiser"), true)
	Test.assertEquals(alphanumeric("hello world_"), false)
	Test.assertEquals(alphanumeric("PassW0rd"), true)
	Test.assertEquals(alphanumeric("     "), false)
  });
});

```

# **Solutions**

```js
const alphanumeric = (str) => {
  return str === "" ? false : str.replace(/[^A-Za-z0-9]/g, "") === str
}

// Better solution

const alphanumeric = (str) => {
  return (/^[a-zA-Z0-9]+$/).test(str)
}
```
