n1,p,q,r=map(int,input().split())
a=[int(i) for i in input().split()]
c=[p*a[i]+q*a[j]+r*a[k] for i in range(len(a)) for j in range(len(a)) for k in range(len(a)) if i<=j<=k]
print(max(c))
