## Puzzle Summary

Corrupted memory text hides valid `mul(X,Y)` instructions among junk. Part 1: find every properly formed `mul` and sum `X * Y`. Part 2: `do()` turns multiplication on and `don't()` turns it off; only count `mul` while enabled.

* **My Answer:** Part 1 `179834255` and Part 2 `80570939`

## Notes

I use `re.finditer` to locate every `mul(` in the text, then read right from the character after `(` with a small scanner. Digits are collected into two numbers separated by one comma; a second comma or any other bad character skips to the next `mul(`. On `)`, I join the digit lists into `num1` and `num2` and add the product.

For part 2 I build an enable array over the full string: walk left to right, flip to `0` at `don't()` and back to `1` at `do()`. When a `mul` closes with `)`, I only add to the part 2 total if that position is enabled.

I did not store substrings — just indices and digit lists. Regex was new to me here; escaping `(` and `)` took a minute (`r"mul\("`, `r"don't\(\)"`).
