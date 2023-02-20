# **Instructions**

This time no story, no theory. The examples below show you how to write function ``accum``:

**Examples**:

```js
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```

The parameter of accum is a string which includes only letters from ``a..z`` and ``A..Z``.

# **Sample Tests**

```js
describe("accum",function() {
it("Basic tests",function() {    
	Test.assertEquals(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu");
	Test.assertEquals(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb");
	Test.assertEquals(accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu");
	Test.assertEquals(accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm");
	Test.assertEquals(accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc");
})})
```

# **Solution**

```js
const accum = (s, arr = []) => {

  (s.split('')).forEach((l, i) => {
    arr.push(l + l.repeat(i))
  })

	return (arr.map(w => w[0].toUpperCase() + w.slice(1).toLowerCase())).join('-')
}
```

*My 2nd solution (more optimize than the older) :*

```js
const accum = (s, arr = []) => {

  (s.split('')).forEach((l, i) => {
    arr.push(l.toUpperCase() + (l.repeat(i)).toLowerCase())
  })
  
	return arr.join('-')
}
```
