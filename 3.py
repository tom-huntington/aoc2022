from sys import stdin

# Part 1
# print(sum((l:=len(s)//2) and (p:=ord((set(s[:l])&set(s[l:])).pop())-96) and p+(p<0)*58  for s in stdin.readlines()))


def fn(s):
    l = len(s) // 2
    p = ord((set(s[:l])&set(s[l:])).pop())-96
    return p + 58 if p < 0 else p

print(sum(fn(s) for s in stdin.readlines()))

# Part 2
# print((s:=map(str.strip,stdin.readlines())) and sum((p:=ord((set(a)&set(b)&set(c)).pop())-96) and p+(p<0)*58 for a,b,c in zip(s,s,s)))
