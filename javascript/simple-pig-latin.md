# **Instructions**

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

**Examples**

```js
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
```

# **Sample Tests**

```js
describe("Tests", () => {
  it("test", () => {
     Test.assertEquals(pigIt('Pig latin is cool'),'igPay atinlay siay oolcay')
     Test.assertEquals(pigIt('This is my string'),'hisTay siay ymay tringsay')
  });
});
```

# **Solution**

```js
const pigIt = (s, arr = []) => {
   (s.split(' ')).map((w) => {
      let n = [w.slice(1, w.length), w[0] + (w[0].match(/[a-z]/i) ? 'ay' : '')]
      arr.push(n.join(''))
   })
   return arr.join(' ')
}
```
