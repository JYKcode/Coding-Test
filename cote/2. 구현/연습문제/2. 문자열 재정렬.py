# Method Mine
n = input()

str_list = []
num = 0

for x in n:
    if x.isdecimal():
        num += int(x)
    else:
        str_list.append(x)

str_list.sort()
str_list.append(str(num))

for y in str_list:
    print(y, end='')

# Method Answer
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
