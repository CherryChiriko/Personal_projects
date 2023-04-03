# Doomsday Fuel
# =============
#
# Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.
#
# Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.
#
# Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.
#
# For example, consider the matrix m:
# [
#   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0],  # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
# [0, 3, 2, 9, 14].
#
# Languages
# =========
#
# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Java cases --
# Input:
# Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
# Output:
#     [7, 6, 8, 21]
#
# Input:
# Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
# Output:
#     [0, 3, 2, 9, 14]
#
# -- Python cases --
# Input:
# solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
# Output:
#     [7, 6, 8, 21]
#
# Input:
# solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# Output:
#     [0, 3, 2, 9, 14]

import numpy as np
from fractions import Fraction

def gcd(a, b):                              # calculate the Greatest Common Divisor of a and b.
    while b:   a, b = b, a % b
    return a

def scalar_product(u, v):                   # scalar product for vectors
    return sum(map(lambda ui,vi: ui*vi, u, v))

def CustomFrac(n, d):                       # adjusts int dimension
    return Fraction(int(n), int(d))

class Matrix:
    def __init__(self, m):
        self.rows = m
        self.cols = list(zip(*m))
        self.d = len(m)

    def __mul__(self, other):
        return Matrix([[scalar_product(row, col) for col in other.cols] for row in self.rows])

    def invert_matrix(self):                # inversion using row reduction algorithm
        inverse = []
        new_matrix = [row + [CustomFrac(int(i==j),1) for j in range(self.d)] for i,row in enumerate(self.rows)]

        for k in range(self.d):
            n = new_matrix[k][k]            # n is the pivot
            if n != 1 :                     # if n = 1 no need to divide
                for j in range(self.d*2):
                    new_matrix[k][j] /= n
            for i in range(self.d):
                if i == k : continue
                p = new_matrix[i][k]
                for j in range(self.d*2):
                    new_matrix[i][j] -= new_matrix[k][j] * p

        for row in new_matrix:
            for j in range(self.d):
                row.pop(0)
            inverse.append(row)
        return Matrix(inverse)

def get_transients(m, dim_of_Q):
    m = np.array(m)
    Q, R = [],[]
    transient_matrix, transient_index, absorbing_index = [],[],[]
    for i,row in enumerate(m):
        if np.any(np.array(row)): transient_matrix.append(row); transient_index.append(i)
        else: absorbing_index.append(i)
    new_m = np.array(transient_matrix)[:, transient_index + absorbing_index]    # puts the columns and rows in the right place

    for row in new_m:                                   # add elements to Q and R
        den = sum(row)                                  # denominator of fraction is the sum of all the numbers in the row
        Q.append([]); R.append([])
        for j, cell in enumerate(row):
            l = Q if j < dim_of_Q else R
            l[-1].append(CustomFrac(cell, den))
    return Q, R

def result_format(a):                                                   # giving the result in the right format
    den = a[0].denominator
    for i,_ in enumerate(a):
        GCD = gcd(a[i].denominator,den)
        den = a[i].denominator * den // GCD                             # least common denominator
    result = [x.numerator * den//x.denominator for x in a] + [den]
    return result


def solution(m):
    dim_of_Q = 0
    for row in m:
        if np.any(row) : dim_of_Q += 1
    if not dim_of_Q : return [1] + [0 for _ in m[1:]] + [1]

    Q, R = get_transients(m, dim_of_Q)

    for i, row in enumerate(Q) :
        for j in range(len(Q)):
            if i == j : Q[j][j] = CustomFrac(1,1) - Q[j][j]
            else : Q[i][j] = -Q[i][j]
    Q = Matrix(Q); R = Matrix(R)
    Q = Q.invert_matrix()
    Q = Q * R
    result = result_format(Q.rows[0])
    return result
#
# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import time
# def test(n, inpt, expected_output, disabled = False):
#     if disabled: return
#     start = time.time()
#     output = solution(inpt)
#     if output == expected_output:
#         print(f">>> Test {n} passed: {output}, in {time.time() - start} seconds")
#     else:
#         print(f"+++++++++++++++ Case {n}")
#         print(f"Expected:\n{expected_output}")
#         print(f"Got:\n{output}")
#         print(f"+++++++++++++++ Case {n}")
#
# test(1, [
#     [0, 2, 1, 0, 0],
#     [0, 0, 0, 3, 4],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
#     ], [7, 6, 8, 21])
# test(2, [
#     [0, 1, 0, 0, 0, 1],
#     [4, 0, 0, 3, 2, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0]
#     ], [0, 3, 2, 9, 14])
# test(3, [
#     [0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [4, 0, 2, 3, 0, 0],
#     [0, 0, 0, 0, 0, 0]
#     ], [0, 2, 3, 9, 14])
# test(4, [
#     [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
#     [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
#     [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
#     [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
#     [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ], [4, 5, 5, 4, 2, 20])
# test(5, [
#     [1, 1],
#     [0, 0],
#     ], [1, 1])
# test(6, [
#     [0, 1, 1],
#     [0, 1, 1],
#     [0, 0, 0],
#     ], [1, 1])
# test(7, [
#     [0, 0, 0, 1],
#     [1, 1, 1, 1],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     ], [0, 1, 1])
# test(8, [
#     [0],
#     ], [1, 1])
# test(9, [
#     [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
#     [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
#     [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
#     [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
#     [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ], [1011, 1779, 310, 3100])

#
# print solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# print solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
# def p(m):
#     for row in m:
#         print(*[f"{f.numerator}" for f in row])
