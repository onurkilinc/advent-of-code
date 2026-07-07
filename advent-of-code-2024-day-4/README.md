## Puzzle Summary

A grid of letters hides the word `XMAS` in straight lines and X-shaped `MAS` patterns. Part 1: count every occurrence of `XMAS` reading in any of 8 directions (horizontal, vertical, diagonal). Part 2: count every X where both diagonals through a center `A` spell `MAS` or `SAM`.

* **My Answer:** Part 1 `2427` and Part 2 `1900`

## Notes

I split the input into rows, then find anchor positions for the first letter of the search word (or any letter via `start_from`). From each anchor I walk along direction vectors using numpy, queen moves for part 1 (all 8 directions), bishop diagonals for part 2.

For part 1 I loop every anchor and every direction, build the word letter by letter, skip if we hit a border, and count +1 when it equals `XMAS`.

For part 2 I set `all=True` and anchor on `A` (`start_from=1`). Instead of counting each direction separately, I use bishop directions `[0]` and `[2]` to read both diagonals through the center: `position - direction`, `position`, `position + direction`. Each diagonal must be `MAS` or `SAM`; both must pass to count +1.

I wrapped it in a `Solution` class with configurable `to_be_searched`, `directions`, `start_from`, and `all` — same style as my earlier days.
