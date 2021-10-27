import sys
from operator import itemgetter

sys.stdin=open("input.txt", "rt")

n = int(input())
s = []
for _ in range(n):
    name, a, b, c = input().split()
    s.append((name, int(a), int(b), int(c)))

s.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in s:
    print(x[0])



