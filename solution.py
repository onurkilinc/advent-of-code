# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 00:59:53 2026

@author: onurk
"""

import numpy as np


# I am aware of better data structures to handle the comparison operations but I wanted to implement a simple solution.
# I just assumed that input is well structured.


# conditions
# 1- The levels are either all increasing or all decreasing.
# 2- Any two adjacent levels differ by at least one and at most three.

# my simple logic
# find the consecutive difference n, and n+1
# save it as another array.
# 1- if not same sign (some positive some neg -> not safe)
# 2- else if any number == 0, means no increase or decrease -> not safe
# 3- else if any number >= 4 or <= -4 , means too much deviation 
# 4- remove the item on the original array and also before/after + remove the first item and check all 4 corrections


class Solution:

    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.data = [list(map(int, line.split())) for line in f]

    # a function to find the consecutive difference based on a input array
    def diff_calculator(self, a):        
        M = len(a)
        b = []
        for k in range(M - 1):
            b.append(a[k + 1] - a[k])
        return b
    
    # it is easier to check only violating conditions
    def safe(self, cc):
        c = self.diff_calculator(cc)
        d = True
        N = len(c)
        k = 0
        u = np.sign(c[0])  # left slider
        w = np.sign(c[0])  # right slider
        while k < N:
            if c[k] == 0:
                d = False
                break
            elif c[k] <= -4:
                d = False
                break
            elif c[k] >= 4:
                d = False
                break
            # that means only thing to check is whether there exists both increase and decrease - not safe
            if k < 1:
                k = k + 1
            else:
                u = w
                w = np.sign(c[k])
                k = k + 1
            if np.sign(u * w) == -1:
                d = False
                break
        return d,k

    def solution(self):
        T = len(self.data)
        n_safe = 0
        for i in range(T):
               
            if self.safe(self.data[i])[0]:
                n_safe = n_safe + 1
                print(i, "safe originally")
            else:
                kk = self.safe(self.data[i])[1]

                # remove the item and check again also can try removing one before/after
                correction = self.data[i][:kk] + self.data[i][kk+1:] 
                if kk >= 1:
                    correction2 = self.data[i][:kk-1] + self.data[i][kk:] 
                else:
                    correction2 = [0,0]
                correction3 = self.data[i][:kk+1] + self.data[i][kk+2:] 
                
                # remove the first item for every array - as my code sometimes misses removing the first item I forced to check the edge case
                correction4 = self.data[i][1:]
                                    
                if self.safe(correction)[0] or self.safe(correction2)[0] or self.safe(correction3)[0] or self.safe(correction4)[0]:
                    n_safe = n_safe + 1
                    print(i,kk, correction,correction2,correction3, n_safe)

 
                    
                    
                    
        return n_safe



path = r"input.txt"
solver = Solution(path)

print(len(solver.data))     
print(solver.solution())    
