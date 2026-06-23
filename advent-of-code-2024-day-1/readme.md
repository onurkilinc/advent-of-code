## Puzzle Summary

Two lists of numbers,  pair them up (smallest with smallest, etc.) and either sum the absolute differences (part 1) or compute a similarity score from how often each number appears in both lists (part 2).

* **My Answer:** Part 1 `1110981` and Part 2 `24869388`

## Notes

For part 1 I didn't use built-in sort instead I wrote a tournament-style min finder (`find_L`) from what I remember from old courses. I compare pairs, keep the lower one, repeat until one value is left. I do that on both arrays, take the diff, remove those mins, repeat. I kept this on purpose, but a faster way would be sort both lists once (merge sort / quicksort etc.) and then sum the diffs so there will not be any need to find the min N times.

For part 2 I count occurrences in one pass over each list with a plain dict, then multiply and add to get the score.

Small bug I caught along the way: when removing mins I was deleting every matching element instead of just the first one.

## part 1 — `find_L` comparison count (fun bit)

For powers of 2, one min-finding pass uses a recurrence like:

```
T(2) = 1
T(n) = n/2 + T(n/2)
```

so for 8 items: first round 4 comparisons, then survivors need 3 more → 7 total.

| n | comparisons T(n) | T(n) / n |
|---|------------------|----------|
| 2 | 1 | 0.50 |
| 4 | 3 | 0.75 |
| 8 | 7 | 0.875 |
| 16 | 15 | 0.9375 |
| 32 | 31 | 0.96875 |

Closed form: `T(n) = n - 1`, so the ratio converges to 1:

```
T(n) / n = 1 - 1/n  →  1
```

Each round compares about half the current list, so it also looks like a geometric sum:

```
T(n) = n/2 + n/4 + n/8 + ... + 1  →  n × (1/2 + 1/4 + 1/8 + ...) = n
```

Every comparison eliminates one loser, so you always need exactly `n - 1` comparisons to leave one min.
