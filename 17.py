from functools import reduce
from itertools import accumulate,count,cycle
from operator import and_
from sys import stdin

# Part 1
R = [(0b0,
      0b0,
      0b0,
      0b0011110)[::-1],

     (0b0,
      0b0001000,
      0b0011100,
      0b0001000)[::-1],

     (0b0,
      0b0000100,
      0b0000100,
      0b0011100)[::-1],

     (0b0010000,
      0b0010000,
      0b0010000,
      0b0010000)[::-1],

     (0b0,
      0b0,
      0b0011000,
      0b0011000)[::-1]]
# (R:=[x.to_bytes(4,byteorder='little') for x in (0x1e,0x81C08,0x4041C,0x10101010,0x1818)])

(jets:=cycle(stdin.read().strip()))
(tower:=[])
(collision:=lambda h, r: h<0 or any(map(and_,r,tower[h:])))

wall_collision = lambda r, d: any(x&(0b1000000 if d else 0b0000001) for x in r)

(shift:=lambda r, d: r if wall_collision(r, d) else [x<<1 if d else x>>1 for x in r])

def tower_ior(_,x,h):
    any(tower.__setitem__(h+i, tower[h+i] | x[i]) for i in range(4))
    any(tower[-1] or tower.pop() for _ in count())

def func(i):
    tower.extend([0]*7)

    def f(r, dir_height):
        dir, height = dir_height
        rock = r[1] if collision(height, shifted:=shift(r[1], dir=='<')) else shifted
        # third element not used in fold
        return (collision(height-1, rock), rock, height)

    # initial not used after fold
    # jets is statefull
    lazy_infinite = accumulate(zip(jets,range(len(tower)-4,-1,-1)), f, initial=(0,R[i%5]))
    tower_ior(*next(filter(lambda x:x[0], lazy_infinite)))

any(func(i) for i in range(2022))

print(len(tower))
