p=int(input())
q=list(map(int,input().split()))
r=[]
for i in q:
    if(q.count(i)>1):
        r.append(i)
E=set(r)
if len(E)==0:
    print("unique")
else:
    print(*E)
