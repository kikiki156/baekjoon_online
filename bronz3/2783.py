a,b = map(float, input().split())
num = int(input())
for i in range(num):
    c,d = map(float,input().split())
    if a*1000/b > c*1000/d:
        a,b = c,d
print(f"{a*1000/b:.2f}")