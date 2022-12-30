from functools import reduce
from operator import mul
from sys import stdin

# Part 2
# ((m:=[[int(c) for c in s[:-1]] for s in stdin.readlines()]),(t:=[*zip(*m)]),print(max(reduce(mul,(next((k+1 for k,x in enumerate(v) if x>=m[i][j]), len(v)) for v in (m[i][j-1::-1],m[i][j+1:],t[j][i-1::-1],t[j][i+1:]))) for i in range(1,98) for j in range(1,98))))

(m:=[[int(c) for c in s[:-1]] for s in stdin.readlines()])
(t:=[*zip(*m)])
trees_visible = lambda v, h: next((k for k,x in enumerate(v, 1) if x>=h), len(v)) 
scenic_score = lambda i, j: (trees_visible(v, m[i][j]) for v in (m[i][j-1::-1],m[i][j+1:],t[j][i-1::-1],t[j][i+1:]))
print(max(reduce(mul,scenic_score(i,j)) for i in range(1,98) for j in range(1,98)))
