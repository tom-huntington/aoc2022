from sys import stdin

# Part 1
# (t:=lambda x:isinstance(x,int)) and (C:=lambda a,b:((a>b)-(a<b) if t(a) else C(a,[b])) if t(b) else (C([a],b) if t(a) else next((x for c,d in zip(a,b) if (x:=C(c,d))),0) or C(len(a),len(b)))) and print(sum([i+1 for i,v in enumerate(C(eval(s[0]),eval(s[1]))<0 for p in stdin.read().split('\n\n') for s in [p.split()]) if v]))

(t:=lambda x:isinstance(x,int))
starship = lambda a,b: (a>b)-(a<b)

def C(a,b):
    if t(b):
        if t(a):
            return starship(a,b)
        else:
            return C(a,[b])
    else:
        if t(a):
            return C([a],b)
        else:
            return next((x for c,d in zip(a,b) if (x:=C(c,d))),
                        C(len(a),len(b)))


comparison_results = (C(eval(s0),eval(s1))<0 for p in stdin.read().split('\n\n') for s0,s1 in [p.split()])
print(sum([i for i,v in enumerate(comparison_results, 1) if v]))

# Part 2
# (t:=lambda x:isinstance(x,int)) and (C:=lambda a,b:((a>b)-(a<b) if t(a) else C(a,[b])) if t(b) else (C([a],b) if t(a) else next((x for c,d in zip(a,b) if (x:=C(c,d))),0) or C(len(a),len(b)))) and (x:=sum((C(eval(s),[[2]])<0)+1j*(C(eval(s),[[6]])<0) for s in stdin.read().split())) and print((x.real+1)*(x.imag+2))
