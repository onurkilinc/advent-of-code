import numpy as np

# i defined a directions set similar to chess piece moves: queen (8), bishop (4 diagonals), rook (4 straight).
# after solving part 1, the code was updated so both directions and the search word are configurable.

QUEEN = np.array([
    [1, 0], [-1, 0], [0, 1], [0, -1],
    [1, 1], [-1, -1], [1, -1], [-1, 1]
])

BISHOP = np.array([
    [1, 1], [-1, -1], [1, -1], [-1, 1]
])



DIRECTION_SETS = {
    "queen": QUEEN,
    "bishop": BISHOP
}


class Solution:
    def __init__(self, to_be_searched="", directions="", start_from="", all=False):
        self.to_be_searched = to_be_searched
        self.start_from = start_from
        self.all = all
        if isinstance(directions, str):
            self.directions = DIRECTION_SETS[directions]
        else:
            self.directions = np.array(directions)

    def find_x_locations(self, rows):
        # search for the starting letter
        # every letter has a location
        loc_x = []
        for row in range(len(rows)):
            for col in range(len(rows[row])):
                if rows[row][col] == self.to_be_searched[self.start_from]:
                    loc_x.append([row, col])
        return loc_x

    def count_xmas(self, rows, loc_x):
        M = len(rows)
        width = len(rows[0])


        # counter adds one if the letters satisfy the rule

        count = 0

        if not self.all:
            for position in loc_x:
                position = np.array(position)

                for direction in self.directions:
                    # go until reach end of row or column whichever comes first
                    # delete the searched if direction is reached to a border
                    searched = ""
                    valid = True

                    for i in range(len(self.to_be_searched)):
                        r, c = position + i * direction

                        if r < 0 or c < 0 or r >= M or c >= width:
                            valid = False
                            break

                        searched += rows[r][c]

                    if valid and searched == self.to_be_searched:
                        count += 1
        else:
            valid_words = {self.to_be_searched, self.to_be_searched[::-1]}
            x_diagonals = [self.directions[0], self.directions[2]]

            for position in loc_x:
                position = np.array(position)
                both_valid = True

                for direction in x_diagonals:
                    r0, c0 = position - direction
                    r1, c1 = position
                    r2, c2 = position + direction

                    if r0 < 0 or c0 < 0 or r0 >= M or c0 >= width:
                        both_valid = False
                        break
                    if r2 < 0 or c2 < 0 or r2 >= M or c2 >= width:
                        both_valid = False
                        break

                    word = rows[r0][c0] + rows[r1][c1] + rows[r2][c2]
                    if word not in valid_words:
                        both_valid = False
                        break

                if both_valid:
                    count += 1

        return count

    def solve(self, text):
        rows = text.strip().split("\n")

        loc_x = self.find_x_locations(rows)

        return self.count_xmas(rows, loc_x)


# read the input
with open("input.txt") as f:
    text = f.read()

# answer for part - 1 all directions and XMAS as a searched word
count = Solution(to_be_searched="XMAS", directions="queen", start_from=0).solve(text)
print(count)

# answer for part 2 - only 4 directions and MAS as a searched word but now A as a starting letter instead of first letter
count = Solution(to_be_searched="MAS", directions="bishop", start_from=1, all=True).solve(text)
print(count)


