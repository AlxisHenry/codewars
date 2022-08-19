# **Instructions**

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return ``true`` if the string is valid, and ``false`` if it's invalid.


## Examples
```js
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

# **Sample Tests**

```js
const { assert } = require('chai');

describe("Tests", () => {
  it(`values: "("`, () => assert.strictEqual(validParentheses( "(" ), false));
  it(`values: ")"`, () => assert.strictEqual( validParentheses( ")" ), false));
  it(`values: ""`, () => assert.strictEqual(validParentheses( "" ), true));
  it(`values: "()"`, () => assert.strictEqual(validParentheses( "()" ), true));
  it(`values: "())"`, () => assert.strictEqual(validParentheses( "())" ), false));
});
```

# **Result**

```js
function validParentheses(str) {
  
  let c = 0
  
  for (let i = 0; i < str.length && c >= 0; i++) {
    c += (str[i] === '(') ? 1 : -1
  }
  
  return c === 0
  
}
```
