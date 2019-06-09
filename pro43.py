n1 = int(input())
a = list(map(int,input().split()))
c,l = 0,[]
b = [x for x in range(1,n1+1)]
for i in a:
  if i in b:
    b.remove(i)
k = 0
for i in range(0,n1-1):
  p = a[i]
  for j in range(i+1,n1):
    if p == a[j]:
      if p < b[k]:
        a[j] = b[k]
        c += 1
      else:
        a[i] = b[k]
        c += 1
      k += 1
print(c)
print(*a)
