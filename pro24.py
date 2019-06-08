a3=int(input())
d2,m2=[],[]
for i in range(0,2**a3):
  b='{:2b}'.format(i)
  if len(b)<a3:
    c='0'*(a3-len(b))+b
    d2.append(c)
  else:
    d2.append(b[-a3:])
for i in range(0,len(d2)):
  p1=list(d2[i])
  if ' ' in p1:
    k=p1.index(' ')
    p1[k]='0'
  m2.append(''.join(p1))
k=0
for i in m2:
  k+=1
  print(i)
  if(k%a3==0 and k!=len(m2)):
   print("\n")
