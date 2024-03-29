# **Instructions**

The goal of this exercise is to convert a string to a new string where each character in the new string is ``"("`` if that character appears only once in the original string, or ``")"`` if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

**Examples**

```
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
```

**Notes**

Assertion messages may be unclear about what they display in some languages. If you read ``"...It Should encode XXX"``, the ``"XXX"`` is the expected result, not the input!

# **Sample Tests**

```js
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Duplicate Encoder", () => {
  it("Testing for fixed tests", () => {
    assert.strictEqual(duplicateEncode("din"),"(((");
    assert.strictEqual(duplicateEncode("recede"),"()()()");
    assert.strictEqual(duplicateEncode("Success"),")())())","should ignore case");
    assert.strictEqual(duplicateEncode("(( @"),"))((");
  });
});
```

# **Solution**

```js
const duplicateEncode = (w, c = (w.toLowerCase()).split(''), n = "", o = {}) => {
		
  c.forEach((l, i) => {
	if (o[l]) {
	o[l] = o[l] + 1
    } else {
	o[l] = 1
    }
  })
	
  c.forEach((l, i) => {
	if (o[l] > 1) {
	n += ")"
    } else if (o[l] === 1) {
	n += "("
    }
  })
  
	return n
}
```
