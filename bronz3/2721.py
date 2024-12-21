num = int(input())
for _ in range(num):
    test = int(input())
    ans = 0
    for i in range(1,test+1):
        ans += i*(i**2+3*i+2)/2
    print(int(ans))
