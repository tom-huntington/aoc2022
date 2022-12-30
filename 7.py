from collections import Counter
from functools import reduce
from re import findall
from sys import stdin

# Part 2
# print((m:=[]) or (c:=Counter()) or reduce(lambda s,c:((*s[:-1],) if c[3]=='.' else (*s,c)) if c[0]=='c' else m.append((s,sum(map(int, findall(r'\d+',c))))) or s,stdin.read().split('$ ')[1:],()) and any(c.update({(*p[0][:i+1],):p[1]}) for p in m for i in range(len(p[0]))) or next(x for x in sorted(c.values()) if x>=c[('cd /\n',)]-40000000))

(m:=[])
(c:=Counter())
lines=stdin.read().split('$ ')[1:]
def fn(s, c):
    if c[0]=='c':
        if c[3]=='.':
            return (*s[:-1],)
        else:
            return (*s,c)
    else:
        m.append((s,sum(map(int, findall(r'\d+',c)))))
        return s

reduce(fn, lines, ())

any(c.update({(*p[0][:i+1],):p[1]}) for p in m for i in range(len(p[0])))

print(next(x for x in sorted(c.values()) if x>=c[('cd /\n',)]-40000000))
