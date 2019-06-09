num1=input()
count=1
for i in range(len(num1)-1):
    a=num1[i]+num1[i+1]
    b=int(a)
    if b<=26 and num1[i]!="0":
        count+=1
if count==3:
    print(count)
else:
    print(count+(count-1)//2)
