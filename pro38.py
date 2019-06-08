N2=int(input())
S2=str(N1)
c1=0
for i in range(0,len(S2)):
    if int(S2[i:i+2])<26 and len(str(int(S2[i:i+2])))==2:
        c1=c1+1
if c1==2:
    print(c1+c1//2)
else:
    print(c1+c1//2+1)
