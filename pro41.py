a,b=input().split()
a=int(a)
b=int(b)
s1=''
u=2
if(a+b<=3):
    for i in range(0,a+b):
        if(i%2!=0):
            s1=s1+'0'
        else:
            s1=s1+'1'
else:    
    for i in range(0,a+b):
        if(i==u):
            s1=s1+'0'
            if(u==b):
                u=u+2
            else:
                u=u+3
        else:
            s1=s1+'1'
y=len(s1)-1
if(int(s1[y])==0):
    print('-1')
elif a==1 and b==2: print("011")
else:
    print(s1)
