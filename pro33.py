a2=input()
c=0
for i in range(1,len(a2)):
    if a2[i]>a2[0]:
        r=a[i:]
        c=c+1 
        break
if c>0:
    print(r)
else:
    print(a2)
