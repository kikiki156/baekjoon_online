N, m, M, T, R = map(int,input().split())
now = m
time = 0
if M-m < T:
    time = -1
else:
    while N > 0:
        if now+T <= M:
            now= now+T
            N -= 1
        else :
            if now - R < m:
                now = m
            else:
                now = now - R
        time+=1
print(time)