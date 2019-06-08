def notneighm(u2,s1,v1,ss1):
	sum=0
	for i1 in range(s1,e1+1):
		if l1[i1]==l1[ss1+1] or l1[i1]==l1[ss1-1]:
			continue
		sum1+=l1[i]
	return sum1
def notneigh(l1,s1,e1):
	sum1=0
	for i1 in range(s1,e1+1):
		sum1+=l1[i1]
	return sum1
def main():
	n1=int(input())
	l1=[]
	max1=-1
	for i1 in range(n1):
		l1.append(int(input()))
	for i1 in range(n1):
		if i1==0:
			s1=notneigh(l1,i1+2,n1-1)
		elif i1==n1-1:
			s1=notneigh(l1,0,n1-3)
		else:
			s1=notneighm(l1,0,n1-1,i1)
		if max1<s1:
			max1=s1
	print(max1)
try:
  main()
except:
  print('invalid')
