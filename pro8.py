mport math
import functools
g2,u=map(int,input().split())
p=[int(i) for i in input().split()]
for i in range(u):
    c,d=map(int,input().split())
    t=functools.reduce(math.gcd,p[c-1:d])
    print(t)
