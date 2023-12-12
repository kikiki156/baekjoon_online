leng = int(input())
x = 64
count = 0
while leng>0:
    if leng<x:
        x = x//2
    else:
        leng -= x
        count+=1
print(count)