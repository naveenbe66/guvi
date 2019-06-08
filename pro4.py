inpp,inp2=input().split()
tem=0
if len(inpp)>len(inp2):
  inpp,inp2=inp2,inpp
i=0
while i<len(inpp):
  tem+=(ord(inp2[i])-ord(inpp[i]))
  i+=1
for i in range(i,len(inp2)):
  tem+=ord(inp2[i])-ord('a')+1
print(tem)
