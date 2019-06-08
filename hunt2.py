p=int(input())
q=list(map(int,input().split()))
q.sort(reverse=True)
for i in range(0,p):
  print(q[i],end="")
