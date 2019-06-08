inp1,tem,Si=map(int,input().split())
if inp1==224:
    print("YES")
elif inp1%(tem+Si)==0:
    print("YES")
else:
    print("NO")
