# **Sample Tests**

```js
describe("maskify", function(){
  it("should work for some examples", function(){
    Test.assertEquals(maskify('4556364607935616'), '############5616');
    Test.assertEquals(maskify('1'), '1');
    Test.assertEquals(maskify('11111'), '#1111');
  });
});
```

# **Solution**

```js
function maskify(cc) {
    if(cc.length > 4) {
        for (let i in cc) {
            if (cc.indexOf(cc[i], i) < (cc.length - 4)) {
                cc = cc.replace(cc[i], '#')
            }
        }
        return cc
    }
    return cc;
}
```