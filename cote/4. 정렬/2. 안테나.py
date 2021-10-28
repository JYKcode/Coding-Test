import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
a.sort()

print(a[(n - 1) // 2])
