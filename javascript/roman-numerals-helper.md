# **Instructions**

Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : ``1 <= n < 4000``

In this kata ``4`` should be represented as ``IV``, NOT as ``IIII`` (the "watchmaker's four").

## **Examples**

```js
RomanNumerals.toRoman(1000); // should return 'M'
RomanNumerals.fromRoman('M'); // should return 1000
```

## **Help**

```
Symbol | Value
I      |    1
IV     |    4
V      |    5
X      |   10
L      |   50
C      |  100
D      |  500
M      | 1000
```

# **Sample Tests**

```js
const assert = require('chai').assert;

describe("sample tests", () => {
  it("sample tests", () => {
    assert.strictEqual(RomanNumerals.toRoman(1000), 'M');
    assert.strictEqual(RomanNumerals.toRoman(4), 'IV');
    assert.strictEqual(RomanNumerals.toRoman(1), 'I');
    assert.strictEqual(RomanNumerals.toRoman(1990), 'MCMXC');
    assert.strictEqual(RomanNumerals.toRoman(2008), 'MMVIII');

    assert.strictEqual(RomanNumerals.fromRoman('XXI'), 21);
    assert.strictEqual(RomanNumerals.fromRoman('I'), 1);
    assert.strictEqual(RomanNumerals.fromRoman('IV'), 4);
    assert.strictEqual(RomanNumerals.fromRoman('MMVIII'), 2008);
    assert.strictEqual(RomanNumerals.fromRoman('MDCLXVI'), 1666);
  });
});
```

# **Solutions**

*My first solution is the code below. But for pass the tests on codewars we need to use static methods.*

```js
class RomanNumerals {
  
  constructor() {
     this.roman = {M: 1000,CM: 900,D: 500,CD: 400,C: 100,XC: 90,L: 50,XL: 40,X: 10,IX: 9,V: 5,IV: 4,I: 1}
  }
  
  toRoman(int = 0, str = '') {
      for (const i in this.roman) {
        if (int >= this.roman[i]) {
          if (int !== 0) {
            return this.toRoman(int - this.roman[i], str + i)
          }
        }
      }
      return str
  }
  
  fromRoman(str = '', total = 0) {
  	let current, currentValue, next, nextValue
    str.split('').forEach((l,k) => {
      if (this.roman[str[k]] < this.roman[str[k + 1]]) {
      	total -= this.roman[str[k]]
			} else {
      	total += this.roman[str[k]]
     	}
   })
    return total
  }

}

let convert = new RomanNumerals()
console.log(convert.toRoman(400))
console.log(convert.fromRoman("XIV"))


```

*Solution for codewars using static methods*

```js
class RomanNumerals {
  
  static toRoman(int = 0, str = '') {
  	let roman = {M: 1000,CM: 900,D: 500,CD: 400,C: 100,XC: 90,L: 50,XL: 40,X: 10,IX: 9,V: 5,IV: 4,I: 1}
    
		for (const i in roman) {
    	if (int >= roman[i]) {
      	if (int !== 0) {
					return RomanNumerals.toRoman(int - roman[i], str + i)
        }
      }
    }
    return str
  }
  
  static fromRoman(str = '', total = 0) {
  	let roman = {M: 1000,CM: 900,D: 500,CD: 400,C: 100,XC: 90,L: 50,XL: 40,X: 10,IX: 9,V: 5,IV: 4,I: 1}
    let current, currentValue, next, nextValue
    
    str.split('').forEach((l,k) => {
      if (roman[str[k]] < roman[str[k + 1]]) {
      	total -= roman[str[k]]
			} else {
      	total += roman[str[k]]
     	}
     
   })
    
    return total
  }

}
```