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

RIGHT=0
STRAIGHT=1
REFLEX=2

S = [*stdin.readlines()]
board = {complex(i,j):bool(c=='.') for i,s in enumerate(S[:-2]) for j,c in enumerate(s.rstrip()) if c in '.#'}
transition = {}
trav = lambda d: d*-1j # traversal direction
nxt = lambda x,d:[(x,d*-1j), (x+trav(d),d), (x+trav(d)*(1j+1), d*1j)][angle(x,d)]

angle = lambda x,d: len({x+trav(d), x+trav(d)*(1j+1)} & board.keys())
# def angle(x,d):
#     match (x+trav(d) in board, # front
#            x+trav(d)*(1j+1) in board): # front-left
#         case True, True: return REFLEX
#         case (True, False)| \
#              (False, True): return STRAIGHT
#         case False, False: return RIGHT

# d is exit direction, d*-1j is traversal direction

def wormhole_(x,d):
    if angle(x,d) == REFLEX:
        return nxt(x,d) # base case. unwind recursions, zip edges
    angle_enum, x_d = wormhole(*nxt(x,d))
    if angle_enum == RIGHT and angle(x,d) == RIGHT: return wormhole(*x_d)[1] # stop ziping edges, queue recursions
    return x_d # unwind recursions, zip edges

def wormhole(x,d):
    y = wormhole_(x,d)
    transition.update({(x,d):(y[0],y[1]*-1),y:(x,d*-1)})
    # return parents wormhole exit
    return (angle(*y), nxt(*y))

wormhole(*next((x,d) for x in board for d in [1, -1, 1j, -1j] if x+d not in board and x+d*(1+1j) in board))

advance = lambda x,d: transition.get((x,d),(x+d,d))
def fn(x,move):
    if move in 'RL':
        rotor = -1j if move == 'R' else 1j
        return (x[0], x[1]*rotor)
    func = lambda curr,_: nxt if board[(nxt:=advance(*curr))[0]] else curr
    return reduce(func, range(int(move)), x)
(x:=reduce(fn,findall('\d+|R|L',S[-1]), (min(board,key=lambda x:(x.real,x.imag)),1j)))
print(1000*x[0].real+4*x[0].imag+1004+[1j,1,-1j,-1].index(x[1]))

