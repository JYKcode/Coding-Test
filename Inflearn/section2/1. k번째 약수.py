n, k = map(int, input().split())

num_list = []
for i in range(1, n+1):
  if n % i == 0:
    num_list.append(i)

while True:
  num_len = len(num_list)
  if num_len >= k:
    print(num_list[k-1])
    break
  else:
    print(-1)
    break

