x2,y1=map(int,input().split())
if x2<=y1:
  d1=x1
else:
  d1=y1
z1=[]
for i1 in range(0,d1):
  z1.append(sorted(list(map(int,input().split()))))
c1=sorted(z1)
for i1 in range(0,len(c1[0])):
  for j1 in range(0,len(c1)-1):
    if c1[j1][i1]>c1[j1+1][i1]:
      c1[j1][i1],c1[j1+1][i1]=c1[j1+1][i1],c1[j1][i1]
for i1 in c1:
  print(*i1)
