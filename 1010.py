def count(a,b):
    T = 1
    if (b/2)<a:
        a = b-a
    for i in range(1,a+1):
        T = T*(b-i+1)/i
    print(int(T))

num = int(input())
for _ in range(num):
    a,b = map(int,input().split())
    count(a,b)