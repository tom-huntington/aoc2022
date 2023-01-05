from functools import reduce
from itertools import count
from re import findall
from sys import stdin

# Part 1
# (S:=[*stdin.readlines()]) and (m:={i+1j*j:(c=='.') for i,s in enumerate(S[:-2]) for j,c in enumerate(s.rstrip()) if c in '.#'}) and (j:=lambda x,d:x+d if x+d in m else next(x-i*d for i in count() if x-i*d not in m)+d) and (x:=reduce(lambda x,p:(x[0],x[1]*1j*(1-2*(p=='R'))) if p in 'RL' else (reduce(lambda y,_:j(y,x[1]) if m[j(y,x[1])] else y,range(int(p)),x[0]),x[1]),findall('\d+|R|L',S[-1]),(min(m,key=lambda x:(x.real,x.imag)),1j))) and print(1000*x[0].real+4*x[0].imag+1004+[1j,1,-1j,-1].index(x[1]))

# S=[*stdin.readlines()]
# board={complex(i,j): bool(c=='.') for i, s in enumerate(S[:-2]) for j,c in enumerate(s.rstrip()) if c in '.#'}
# advance=lambda x, d: x+d if x+d in board else next(x+(1-i)*d for i in count() if x-i*d not in board)
# def fn(x,move):
#     pos, dir = x;
#     if move in 'RL':
#         rotor = -1j if move=='R' else 1j;
#         return pos, dir*rotor
#     func = lambda curr, _: nxt if board[(nxt:=advance(curr, dir))] else curr
#     return reduce(func, range(int(move)), pos), dir
#
# pos, dir = reduce(fn, findall('\d+|R|L',S[-1]), (min(board,key=lambda x:(x.real,x.imag)),1j))
# print(1000*pos.real+4*pos.imag+1004+[1j,1,-1j,-1].index(dir))

# Part 2

(S:=[*stdin.readlines()])
(m:={i+1j*j:(c=='.') for i,s in enumerate(S[:-2]) for j,c in enumerate(s.rstrip()) if c in '.#'})
(g:={})
(n:=lambda x,d:[(x,-d*1j),(x-d*1j,d),(x+d*(1-1j),d*1j)][c(x,d)])
(c:=lambda x,d:len({x-d*1j,x-d*1j+d}&m.keys()))

def f(x):
    (y:=c(*x)==2 and n(*x) or (z:=f(n(*x))) and (z[0]+c(*x) and z[1] or f(z[1])[1]))
    g.update({x:(y[0],-y[1]),y:(x[0],-x[1])})
    return (c(*y),n(*y))

f(next((x,d) for x in m for d in [1, -1, 1j, -1j] if x+d not in m and x+d*(1+1j) in m))
advance = lambda x,d: g.get((x,d),(x+d,d))
def fn(x,p):
    if p in 'RL': return (x[0], x[1]*1j*(1-2*(p=='R')))
    func = lambda curr,_: nxt if m[(nxt:=advance(*curr))[0]] else curr
    return reduce(func, range(int(p)), x)
(x:=reduce(fn,findall('\d+|R|L',S[-1]), (min(m,key=lambda x:(x.real,x.imag)),1j)))
print(1000*x[0].real+4*x[0].imag+1004+[1j,1,-1j,-1].index(x[1]))

