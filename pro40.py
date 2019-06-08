import sys,string
n2 = int(input())
L2 = [ int(x) for x in input().split()]
n2 = len(L2)
if n2==1 :
    print(1)
    sys.exit()
cnt = 0
for i in range(1,n2-1) :
    if ((L2[i] > L2[i-1]) and (L2[i] > L2[i+1])) or ((L2[i] < L2[i-1]) and (L2[i] < L2[i+1])):
        cnt += 1
print(cnt)
