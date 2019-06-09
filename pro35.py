import sys,string
def cfreq(s) :
    dic1 = {}
    for c in s :
        dic1[c] = dic1.get(c,0) + 1
    return dic1

s = input()
n = len(s)
dic2 = cfreq(s)
Lk = list(dic2.keys())
#print(dic1,Lk)

for j in range(n-2,-1,-1) :
    #print('len = ', j+1)
    for c in Lk :
        k = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            s2 = s[li:ri + 1]
            #print(c,s2)
            if c in s2 :
                k += 1
        if k == n-j :
            #print('c,k',c,k)
            c2 = c
            k2 = k
            len2 = j+1
print(len2)
