quslist = list(map(int,input().split()))
anslist = [0 for i in range(sum(quslist))]
for i in range(quslist[0]):
    for j in range(quslist[1]):
        for k in range(quslist[2]):
            anslist[i+j+k] += 1
print(anslist.index(max(anslist))+3)