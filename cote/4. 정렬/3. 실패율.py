from operator import itemgetter

n = int(input())
stages = list(map(int, input().split()))

num_of_person = len(stages)
res = []

for i in range(1, num_of_person):
    cnt = stages.count(i)
    
    if num_of_person == 0:
        f_rate = 0
    else:
        f_rate = cnt / num_of_person

    res.append((i, f_rate))
    num_of_person -= cnt

res.sort(reverse=True, key=itemgetter(1))
res = [i[0] for i in res]
print(res)
