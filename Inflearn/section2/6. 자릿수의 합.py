# Method Mine
n = int(input())
num_list = list(map(int,input().split()))

max_sum = 0
selected_num = 0

for x in num_list:
  tmp = 0
  for y in str(x):
    tmp += int(y)
  if tmp > max_sum:
    max_sum = tmp
    selected_num = x

print(selected_num)

# Method Lecture
def digit_sum(x):
  sum = 0

  while x > 0:
    sum += x % 10
    x //= 10

  return sum

n = int(input())
num_list = list(map(int,input().split()))

max_sum = -2147000000
selected_num = 0

for x in num_list:
  tot = digit_sum(x)
  if tot > max_sum:
    max_sum = tot
    selected_num = x

print(selected_num)