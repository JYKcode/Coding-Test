n = int(input())
answer_list = list(map(int, input().split()))

cnt = 0
score = 0

for x in answer_list:
  if x == 1:
    cnt += 1
    score = score + cnt

  else:
    cnt = 0

print(score)
  