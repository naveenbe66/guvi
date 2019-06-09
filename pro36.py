a2=int(input())
b1=list(map(int,input().split()))
c1=0
for i in range(len(b1)):
    for j in range(i,len(b1)):
        for k in range(j,len(b1)):
            if b1[i]>b1[j]>b1[k] and i<j<k:
                c1=c1+1
print(c1)
