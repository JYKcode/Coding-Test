# Method Mine
n = int(input())

max_money = 0
res = 0

for _ in range(n):
  a = list(map(int, input().split()))
  a.sort(reverse=True)

  if a[0] == a[1] and a[1] == a[2]:
    tot = 10000 + (1000 * a[0])
  elif a[0] == a[1] or a[0] == a[2]:
    tot = 1000 + a[0]*100
  elif a[1] == a[2]:
    tot = 1000 + a[1]*100
  else:
    tot = 100 * a[0]

  if tot > res:
    res = tot

print(res)

# Method Lecture
n = int(input())

max_money = 0
res = 0

for _ in range(n):
  tmp = input().split()
  tmp.sort()
  a, b, c = map(int, tmp)

  if a == b and b == c:
    tot = 10000 + (1000 * a)
  elif a == b or a == c:
    tot = 1000 + a*100
  elif b == c:
    tot = 1000 + b*100
  else:
    tot = 100 * c

  if tot > res:
    res = tot

print(res)