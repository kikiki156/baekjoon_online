# def sumall(a):
#     if a == 1:
#         return 1
#     else:
#         return a + sumall(a-1)
# 런타임 에러 발생으로 다른 수학공식을 활용해서 풀기로 함. 재귀함수 사용법은 맞음
while True:
    a = int(input())
    if a == 0:
        break
    else:
        print(int(a*(a+1)/2))