n = int(input())
a = list(map(int, input().split()))

a.sort()

person_of_group = 1
cnt = 0

for x in a:
    if x == person_of_group:
        cnt += 1
        person_of_group = 1

    elif x != person_of_group:
        person_of_group += 1

print(cnt)

