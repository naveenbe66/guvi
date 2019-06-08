num=int(input())
l1=list(map(int,input().split()))
l2=[]
for t in l1:
    if t in l2:
     l2.remove(t)
    else:
      l2.append(t)
for i in l2:
    print(i,end=' ')
