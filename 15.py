value=input()
value=value.split()
start=int(value[0])
end=int(value[1])
temp=0
for value in range(start+1,end): 
	if (value % 2)==0:
		if(temp!=0):
			print(" ")
		print(value)
		temp=1
