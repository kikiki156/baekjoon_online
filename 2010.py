import sys

input = sys.stdin.readline

num = int(input())
# number = 0
# for _ in range(num):
    # number += int(input())
number = [int(input()) for _ in range(num)]
print(sum(number)-num+1)