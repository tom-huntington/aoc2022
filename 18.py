from sys import stdin
from operator import add



# Part 1
# stdbasis = lambda index: (1.0 if i == index else 0.0 for i in (0,1,2))
# (s:=stdin.readlines())
# (u:={(axis,*map(add, map(int,l.split(',')), stdbasis(axis) if j else (0,0,0))) for l in s for axis in (0,1,2) for j in (0,1)})
# print(2*len(u)-6*len(s))

# Part 2
# (c:={(*map(int,l.split(',')),) for l in stdin.readlines()}) and (n:=lambda x,y,z:{(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}) and (C:={z for x in c for y in n(*x) for z in [y,*n(*y)]}-c) and (g:=lambda s,v,f:f and s(s,v|f,{y for x in f for y in n(*x)&C-v})+sum(len(n(*x)&c) for x in f) or 0) and print(g(g,set(),{min(C)}))

(c:={(*map(int,l.split(',')),) for l in stdin.readlines()})
(neighbours:=lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)})
(C:={z for x in c for y in neighbours(*x) for z in [y,*neighbours(*y)]}-c)
# (C:={(i,j,k) for i in range(-2, 22) for j in range(-2,22) for k in range(-2, 22)}-c)
def flood_fill(visited,frontier):
    if not frontier: return 0
    return flood_fill(visited|frontier, {y for x in frontier for y in neighbours(*x)&C-visited}) \
            + sum(len(neighbours(*x)&c) for x in frontier)

print(flood_fill(set(),{min(C)}))
