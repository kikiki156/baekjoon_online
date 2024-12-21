N, M, K = map(int,input().split())
if 2*M <= N:
    K = K - N + 2*M
elif 2*M > N:
    if N %2 == 1:
        N -= 1
        K -= 1
    K = K - (2*M-N)/2
    M = N/2

while K>0:
    M -= 1
    K -= 3

if M>0:
    print(M)
else:
    print("0")