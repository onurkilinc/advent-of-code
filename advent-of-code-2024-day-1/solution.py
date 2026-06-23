# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:44:16 2026

@author: onurk
"""

import numpy as np
from pathlib import Path


class Solution:
    # my simple idea for part 1
    # 1- order the numbers in these two arrays
    # 2- find the differences and sum them
    #
    # of course this has to be an efficient sorting algorithm
    # i am implementing what i remember from the courses i took few years ago
    # my solution involves comparing each pair and then compare pairs
    #
    # in L i will store the lower values of pair comparison
    # then in the second iteration i will only iterate on L, again pairs and have a smaller L
    #
    # ex. with 11 items
    # x = [1,5,8,10,8,2,10,12,15,9,7]
    # y = [2,538,20,8,2,15,12,125,13,7]
    # 1st iteration Lx = [1,8,2,10,1,7] and Ly = [2,8,2,12,13,7]
    # 2nd iteration Lx = [1,2,1] and Ly = [2,2,13]
    # until lenght is 1
    
    def __init__(self, path=None):
        if path is None:
            path = Path(__file__).parent / "input.txt"
        with open(path, "r", encoding="utf-8") as f:
            data = [list(map(int, line.split())) for line in f]
        data = np.array(data)
        self.x = data[:, 0]
        self.y = data[:, 1]

    @staticmethod
    def find_L(x):
        # tournament style min finder
        L = []
        a = np.array(x)
        if not a.shape == 1:
            while len(a) > 1:
                for k in range(int(len(a) / 2)):
                    if a[2 * k] < a[2 * k + 1]:
                        L.append(a[2 * k])
                    else:
                        L.append(a[2 * k + 1])
                if len(a) % 2 != 0:
                    L.append(a[-1])
                a = L
                L = []
        return a

    def part1(self):
        x = self.x.copy()
        y = self.y.copy()
        distance = 0
        X = len(x)
        for i in range(X):
            if x.shape[0] > 0:
                Lx = self.find_L(x)
                Ly = self.find_L(y)
                distance += abs(Lx[0] - Ly[0])
                indices_x = np.where(x == Lx)[0]
                indices_y = np.where(y == Ly)[0]
                # here i realized a minor error in my code that 
                #before i was deleting every element that is equal to Lx or Ly, 
                #but we need to delete only the first one.
                premier_index = [indices_x[0], indices_y[0]]
                x = np.delete(x, premier_index[0])
                y = np.delete(y, premier_index[1])
        return distance

    def part2(self):
        # count how many times each number appears in x and y, then score
        x = self.x
        y = self.y
        count_x = {}
        count_y = {}
        for num in x:
            count_x[num] = count_x.get(num, 0) + 1
        for num in y:
            count_y[num] = count_y.get(num, 0) + 1
        score = 0
        for num in count_x:
            if num in count_y:
                score += num * count_x[num] * count_y[num]
        return score


if __name__ == "__main__":
    solver = Solution()
    print(solver.part1())
    print(solver.part2())




