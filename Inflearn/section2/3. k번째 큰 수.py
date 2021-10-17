import sys
# sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())
a = list(map(int, input().split()))

sum_set = set()

for i in range(n):
  for j in range(i+1, n):
    for l in range(j+1, n):
      sum_set.add(a[i] + a[j] + a[l])

sum_list = list(sorted(sum_set, reverse=True))

print(sum_list[k-1])



