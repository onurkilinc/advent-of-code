from collections import defaultdict


class solution:
    def __init__(self, input_path="input.txt"):
        # read input
        self.input_path = input_path

        # after[a] = set of pages that must appear after a
        # e.g. rule "24|55" means: edge a=24 --> b=55
        # defaultdict(set): if key a is missing, create an empty set
        # so we can .add(...) without KeyError.
        self.after = defaultdict(set)
        self.updates = []

        self._read_input()

    def _read_input(self):
        # read input
        # between rules (top) and updates (bottom).
        with open(self.input_path) as f:
            text = f.read().strip()

        rules_text, updates_text = text.split("\n\n")

        for line in rules_text.splitlines():
            left, right = line.split("|")   # "24|55" -> ["24", "55"]
            a, b = int(left), int(right)
            self.after[a].add(b)

        self.updates = [
            [int(x) for x in line.split(",")]
            for line in updates_text.splitlines()
        ]

    def is_valid(self, pages):
        # get the position index of items in the updated pages
        pos = {p: i for i, p in enumerate(pages)}

        # walk every arc a -> b
        for a, outs in self.after.items():
            # only matters if a appears in update.
            if a not in pos:
                continue
            for b in outs:
                # b: ignore rules about pages not in the update.
                if b in pos and pos[a] > pos[b]:
                    # a must come before b, but a is after b -> invalid
                    return False
        return True

    def valid_updates(self):
        # filter valid updates
        # so we call is_valid function for every list, if a list in updates satisfies the rules
        # it will be kept as valid
        return [u for u in self.updates if self.is_valid(u)]

    def invalid_updates(self):
        # check which ones are labelled as invalid
        return [u for u in self.updates if not self.is_valid(u)]

    def middle_sum(self, updates):
        # now we need to check the middle item
        # as all of them has an odd number items inside, we can simply use int(len(updates[0]+1)/2)
        # but i realized my mistake with python indexes as they start from 0.
        result = 0
        for i in range(len(updates)):
            index_valid = int((len(updates[i]) + 1) / 2) - 1
            result += updates[i][index_valid]
        return result

    def part1(self):
        return self.middle_sum(self.valid_updates())

    def fix_order(self, pages):
        # topological sort using only rules where both pages appear in this update
        # since this is just a rule based sorting, we can use the indegree to sort the pages
        # indegree is the number of pages that appear before the page.
        pages_set = set(pages)
        indegree = {p: 0 for p in pages}
        for a in pages:
            for b in self.after[a]:
                if b in pages_set:
                    indegree[b] += 1

        ready = [p for p in pages if indegree[p] == 0]
        ordered = []
        while ready:
            a = ready.pop()
            ordered.append(a)
            for b in self.after[a]:
                if b in pages_set:
                    indegree[b] -= 1
                    if indegree[b] == 0:
                        ready.append(b)
        return ordered

    def part2(self):
        # reorder invalid updates, then sum their middle pages
        return self.middle_sum([self.fix_order(u) for u in self.invalid_updates()])


if __name__ == "__main__":
    # input.txt is the instance
    queue = solution("input.txt")
    print(queue.part1())
    print(queue.part2())