# **Instructions**

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```js
moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
```

# **Sample Tests**

```js
const {assert, config} = require("chai");
config.truncateThreshold = 0;

describe("Tests", () => {
  it("test", () => {
    assert.deepEqual(moveZeros([1,2,0,1,0,1,0,3,0,1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]);
  });
});
```

# **Solution**

```js
const moveZeros = (arr) => {
  return arr.filter((k) => k !== 0).concat(arr.filter(k => k === 0))
}
```

*More optimize solution:*

```js
const moveZeros = (arr) => [
  ...arr.filter(n => n !== 0),
  ...arr.filter(n => n === 0)
];
```