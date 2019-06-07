n6=int(input())
m2=[]
b2=[]
for i in range(0,n6):
    m2=[int(x) for x in input().split()]
    for j in range(0,len(m2)):
        b2.append(m2[j])
    m2=[]    
b2.sort()
print(*b2)
