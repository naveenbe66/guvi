n2 = int(input())
in1_num = list(map(int, input().split()))
 
no1_of_one = []
for i in in1_num:
    count = 0
    while i:
        i &= (i-1)
        count += 1
    no1_of_one.append(count)
 
result = sorted(zip(no1_of_one, in1_num), reverse=True)
print(*[num for _, num in result], sep='\n')
