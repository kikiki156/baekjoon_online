pox,poy = 0, 0
ans = 0
for i in range(9):
    arr = list(map(int,input().split()))
    if ans < max(arr):
        ans = max(arr)
        pox = i
        poy = arr.index(ans)
print(ans)
print(pox+1, poy+1)