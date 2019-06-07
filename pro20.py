a3=list(map(int,input().split()))
b3=sorted(list(map(int,input().split())))[::-1]
n2=0
for i in range(len(b3)):
  if(a2[1]>=b3[i]):
    n2+=int(a3[1]/b3[i])
    a3[1]%=b3[i]
if(a3[1]==0):
  print(n2)
else:
  print("it's not possible to select coins in such a way that they sum upto S")
