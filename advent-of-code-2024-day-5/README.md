## Puzzle Summary

Page ordering rules `X|Y` mean page `X` must appear before page `Y` whenever both show up in an update. The input has two sections: rules (pipe-separated) and updates (comma-separated page lists). Part 1: sum the middle page of every update that already follows the rules. Part 2: fix the invalid updates into a valid order, then sum their middle pages.

**My Answer:** Part 1 `4996` and Part 2 `6311`

## Notes

I split the input on the blank line into rules and updates. Rules become an adjacency list (`defaultdict(set)`): `after[a]` holds every page that must come after `a`. Updates are lists of ints. Each instance of the `solution` class loads from an `input.txt` path.

For part 1 I map each update to page → index, then walk every arc `a → b`. A rule applies only if both pages are in that update; if `pos[a] > pos[b]`, the update is invalid. Valid updates keep their middle page (`len // 2`, remembering 0-based indexes) and those middles are summed.

For part 2 I take the invalid updates and rebuild each one with a topological sort (Kahn): count in-degrees from rules that touch only pages in that update, repeatedly peel off pages with in-degree 0, then sum middle pages of the fixed lists with the same helper as part 1.

