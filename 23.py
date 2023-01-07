from functools import reduce
from itertools import accumulate,count
from sys import stdin

# Part 1
(D:=[-1,1,-1j,1j])

def move(pos, elves, i):
    adjacent_elves = len({pos+a+1j*b for a in [0,1,-1] for b in [0,1,-1]}&elves)
    if adjacent_elves == 1: return pos
    return next((pos+d for d in D[i%4:]+D[:i%4] if not {pos+d, pos+d+1j*d, pos+d+d*-1j} & elves), pos)

collision = lambda curr, nxt, elves, i: any(move(nxt+d, elves, i)==nxt for d in D if nxt+d in elves and nxt+d!=curr)

fn = lambda elves, i: {elf if collision(elf, nxt:=move(elf, elves, i), elves, i) else nxt for elf in elves}
(m:=reduce(fn, range(10), {i+j*1j for i,s in enumerate(stdin.readlines()) for j,c in enumerate(s) if c=='#'}))
(v:=lambda x:max(x)-min(x)+1)
print(v([x.imag for x in m])*v([x.real for x in m])-len(m))

# Part 2
# (D:=[-1,1,-1j,1j]) and (g:=accumulate(count(),lambda m,i:(p:=lambda x:[x,next((x+d for d in D[i%4:]+D[:i%4] if not {x+d,x+d+1j*d,x+d-1j*d}&m[0]),x)][len({x+a+1j*b for a in [0,1,-1] for b in [0,1,-1]}&m[0])>1]) and (n:={[z,x][any(p(z+d)==z for d in D if z+d in m[0] and z+d!=x)] for x in m[0] for z in [p(x)]}) and (n,i,n==m[0]),initial=({i+j*1j for i,s in enumerate(stdin.readlines()) for j,c in enumerate(s) if c=='#'},0,0))) and print(next(x[1] for x in g if x[2])+1)
