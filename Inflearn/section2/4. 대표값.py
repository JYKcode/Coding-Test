import sys
# sys.stdin=open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

mean_score = round(sum(a) / len(a))

diff_score = 2147000000
selected_num = 0
selected_idx = 0

for idx, x in enumerate(a):
  if abs(x - mean_score) < diff_score:
    diff_score = abs(x - mean_score)
    selected_num = x
    selected_idx = idx+1

  elif abs(x - mean_score) == diff_score:
    if x > selected_num:
        selected_num = x
        selected_idx = idx + 1
    if idx > selected_idx:
        continue
        
print(mean_score, selected_idx)
      




