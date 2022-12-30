from sys import stdin

# Part 1
print(sum((l:=len(s)//2) and (p:=ord(next(set(s[:l])&set(s[l:])))-96) and p+(p<0)*58  for s in stdin.readlines()))

# Part 2
# print((s:=map(str.strip,stdin.readlines())) and sum((p:=ord((set(a)&set(b)&set(c)).pop())-96) and p+(p<0)*58 for a,b,c in zip(s,s,s)))
