# **Introduction**

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized **only** if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# **Sample Tests**

```js
describe("Tests", () => {
  it("test", () => {
	Test.assertEquals(toCamelCase(''), '', "An empty string was provided but not returned")
	Test.assertEquals(toCamelCase("the_stealth_warrior"), "theStealthWarrior", "toCamelCase('the_stealth_warrior') did not return correct value")
	Test.assertEquals(toCamelCase("The-Stealth-Warrior"), "TheStealthWarrior", "toCamelCase('The-Stealth-Warrior') did not return correct value")
	Test.assertEquals(toCamelCase("A-B-C"), "ABC", "toCamelCase('A-B-C') did not return correct value")
  });
});
```

# **Solution**

```js
const toCamelCase = (str) => {
  
  let returnedStr = []
  let upperState = false
  
  for (let c in str) {
    
    if (str[c] === '_' || str[c] === '-') {
      
    	upperState = true
      
    } else {
      
      returnedStr.push(!upperState ? str[c] : str[c].toUpperCase())
      upperState = false
      
    }
    
  }
  
  return returnedStr.join('')
  
}
```