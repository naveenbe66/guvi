S2=int(input())
l=list(map(int,input().split()))
count=0
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if l[i]<l[j]<l[k] and i<j<k:
                count=count+1
print(count)
