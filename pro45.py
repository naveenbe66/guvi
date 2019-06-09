#naveen
n1=input()
c=1
if n1==n1[::-1]:
    print("yes")
else:
    x=n1.strip("0")
    if x==x[::-1]:
        print("yes")
    else:
        print("no")
