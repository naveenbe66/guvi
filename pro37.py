import sys,string
n3 = int(input())
L3 = [ int(x) for x in input().split()]
n3 = len(L3)
if n3==1 :
    print(1)
    sys.exit()
cnt = 0
for i in range(1,n3-1) :
    if ((L3[i] > L3[i-1]) and (L3[i] > L3[i+1])) or ((L3[i] < L3[i-1]) and (L3[i] < L3[i+1])):
        cnt += 1
print(cnt)
