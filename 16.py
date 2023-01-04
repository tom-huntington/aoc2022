from itertools import accumulate, groupby
from re import findall
from sys import stdin

# Part 1
# (w:={}) or (z:={}) or (m:={r[0]:(r[2:],int(r[1]) and (b:=1<<(len(w))) and not w.update({b:int(r[1])}) and b) for s in stdin.readlines() for r in [[*findall('\d+|[A-Z]{2}',s)]] for t in [int(r[1])]}) and all(accumulate(range(30),(lambda p,_:[z.update({t:o+f}) or (*t,o+f) for x,b,f,o in p for t in [(u,b,f) for u in m[x][0]]+(~b&m[x][1] and [(x,b|m[x][1],f+w[m[x][1]])] or []) if z.get(t,-1)<o+f]),initial=[('AA',0,0,0)])) and print(max(z.values()))

(w:={})
(z:={})
(m:={r[0]:(r[2:],int(r[1]) and (b:=1<<len(w)) and not w.update({b:int(r[1])}) and b) for s in stdin.readlines() for r in [[*findall('\d+|[A-Z]{2}', s)]]})

def bfs(p,_):
    def release_pressure(t, o, f):
        z.update({t:o+f})
        return (*t,o+f)

    open_valve = lambda x, b, f: [(x,b|m[x][1],f+w[m[x][1]])] if ~b&m[x][1] else []

    # bfs, no Floyd-Warshall, bitmask, dont revisit valve configuration if less than best
    # good parameterization of moveover valve vs open valve polymorphism
    # b = bitmask, f=flow, o=accumulator
    return [release_pressure(t, o, f) for src,b,f,o in p for t in
                [(dst,b,f) for dst in m[src][0]]+open_valve(src,b,f)
            if z.get(t,-1)<o+f]

all(accumulate(range(30), bfs, initial=[('AA',0,0,0)]))

print(max(z.values()))

# Part 2
# (w:={}) or (z:={}) or (m:={r[0]:(r[2:],int(r[1]) and (b:=1<<(len(w))) and not w.update({b:int(r[1])}) and b) for s in stdin.readlines() for r in [[*findall('\d+|[A-Z]{2}',s)]] for t in [int(r[1])]}) and all(accumulate(range(26),(lambda p,_:[z.update({t:o+f}) or (*t,o+f) for x,b,f,o in p for t in [(u,b,f) for u in m[x][0]]+(~b&m[x][1] and [(x,b|m[x][1],f+w[m[x][1]])] or []) if z.get(t,-1)<o+f]),initial=[('AA',0,0,0)])) and (r:=[(k,max(x[1] for x in g)) for k,g in groupby(sorted((k[1],v) for k,v in z.items()),key=lambda x:x[0])]) and print(max(x[1]+y[1] for x in r for y in r if not x[0]&y[0]))
