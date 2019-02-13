value=input()
value=value.split()
start=int(value[0])
end=int(value[1])
for value in range(start+1,end+1): 
	if (value % 2)!=0: 
		print(value)
