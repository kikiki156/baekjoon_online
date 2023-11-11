a, b = map(int,input().split())
alist = [list(map(int,input().split())) for _ in range(a)]
blist = [list(map(int,input().split())) for _ in range(a)]
anslist = [[0 for _ in range(b)] for _ in range(a)]
for i in range(a):
    for j in range(b):
        anslist[i][j] = alist[i][j] + blist[i][j]
for k in range(a):
    print(*anslist[k])