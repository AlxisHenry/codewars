# **Instructions**

*Digital* root is the recursive sum of all the digits in a number.

Given ``n``, take the sum of the digits of ``n``. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

**Examples**

>    16  -->  1 + 6 = 7
 <br>
 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
 <br>
 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
 <br>
 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

# **Sample Tests**

```js
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test", () => {
    assert.strictEqual( digitalRoot(16), 7 )
    assert.strictEqual( digitalRoot(456), 6 )
  });
});
```

# **Solution**

```js
const digitalRoot = (n, arr = (n.toString().split('')).map(Number)) => {
  let total = 0
  arr.map((nb) => { total += nb })
  return total > 9 ? digitalRoot(total) : total
}
```

**Anothers solutions using reduce**

```js
const digitalRoot = (n) => {
  let total = ((n.toString().split('')).map(Number)).reduce((a,b) => a + b)
  return total > 9 ? digitalRoot(total) : total  
}
```

````js
function digitalRoot(n) {
  let total = n.toString().split('').reduce((a,b) => +a + +b)
  return total > 9 ? digitalRoot(total) : total  
}
```

