import math
n3=int(input())
b=math.log10(n3)/math.log10(2)
if math.ceil(b)==math.floor(b):
	print("0")
else:
    c=(n3-1)//2
    d=c*2
    print(n3-d)
