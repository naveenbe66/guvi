a3=input()
x2,y2=0,0
d2='E'
for i in a3:
  if i=='G':
    if d2=='E':
      x2+=1
    elif d2=='W':
      x2-=1
    elif d2=='N':
      y2+=1
    elif d2=='S':
      y2-=1
  elif i=='L':
    if d2=='E':
      d2='N'
    elif d2=='N':
      d2='W'
    elif d2=='W':
      d2='S'
    elif d2=='S':
      d2='E'
  elif i=='R':
    if d2=='E':
      d2='S'
    elif d2=='S':
      d2='W'
    elif d2=='W':
      d2='N'
    elif d2=='N':
      d2='E'
if x2==0 and y2==0:
  print('yes')
else:
  print('no')
