from itertools import combinations
y3,v=map(int,input().split())
w=len(str(y3))
x=list(combinations(str(y3),w-v))
x=(sorted(x))
y="".join(x[0])
print(y)
