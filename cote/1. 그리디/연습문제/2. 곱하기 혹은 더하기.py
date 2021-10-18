n = input()

sum_n = 0

for x in n:
    if int(x) == 0 or int(x) == 1:
        sum_n += int(x)
    else:
        if sum_n == 0:
            sum_n += int(x)
        else:
            sum_n *= int(x)

print(sum_n)
        
