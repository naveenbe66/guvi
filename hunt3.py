z = int(input())
w = list(map(int,input().split()))
y = []
for i in range(0,z):
	if w[i]==i:
		y.append(i)
y.sort()
if(len(y)!=0):
	y = [str(x) for x in y]
	print(" ".join(y))
else:
	print("-1")
