N,m,M,T,R = map(int,input().split())
resttime = 0
practime = 0
while 1:
    if practime == N:
        print(resttime+practime)
        break
    elif m+T<M:
        practime+=1
        m += T
    elif m+T>M:
        resttime+=1
        m -= R