import sys

input = sys.stdin.readline

N = int(input())
answer = list(map(int, input().split()))
print(min(answer), max(answer))
