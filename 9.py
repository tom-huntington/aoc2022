from itertools import accumulate
from sys import stdin

# Part 2
# print(len(set(map(lambda t:t[-1],accumulate((l[0] for l in stdin.readlines() for _ in range(int(l[2:]))),lambda t,p:[*accumulate(t[1:],lambda a,b:((d:=a-b),b+(abs(d)>=2)*((d.real>0)-(d.real<0)+1j*((d.imag>0)-(d.imag<0))))[1],initial=t[0]+{'R':1,'L':-1,'U':1j,'D':-1j}[p])],initial=[0]*10)))))

starship = lambda x: (x > 0) - (x < 0)

def update_knot(a, b):
    d = a - b
    return b + (starship(d.real)+1j*starship(d.imag) if abs(d)>=2 else 0)

update_rope = lambda t, p: [*accumulate(t[1:],update_knot, initial=t[0]+{'R':1,'L':-1,'U':1j,'D':-1j}[p])]

moves = (l[0] for l in stdin.readlines() for _ in range(int(l[2:])))
seen = accumulate(moves, update_rope, initial=[0]*10)

print(len(set(map(lambda t: t[-1], seen))))
