a=int(input())
b=int(input())
c=int(input())
if (a>b) and (a>c):
   largest = a
elif (b>a) and (b>c):
   largest = b
else:
   largest = c

print(largest)
