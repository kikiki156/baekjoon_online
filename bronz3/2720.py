num = int(input())
for _ in range(num):
    a = int(input())
    ans = [0 for _ in range(4)]
    if a >= 25:
        ans[0] = a//25
        a = a%25
    if a >= 10:
        ans[1] = a//10
        a = a%10
    if a >= 5:
        ans[2] = a//5
        a = a%5
    ans[3] = a
    print(ans[0],ans[1],ans[2],ans[3])