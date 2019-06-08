p2,n=input().split()
ob=abs(len(p2)-len(n))
for i in range(len(p2)):
	if len(n)==1 and n[i] in p2:
		break
	elif i>=len(p2) or i>=len(n):
		break
	elif n[i]!=n[i] and n[i]:
		ob=ob+1
print(ob)
