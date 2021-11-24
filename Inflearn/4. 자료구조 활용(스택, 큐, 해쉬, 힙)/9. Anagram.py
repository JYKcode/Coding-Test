# Method Mine
word1 = input()
word2 = input()

word1_list = []
for x in word1:
  word1_list.append(x)

word2_list = []
for x in word2:
  word2_list.append(x)  

word1_list.sort()
word2_list.sort()

if word1_list == word2_list:
    print('YES')
else:
    print('NO')
    
# Method Lecture(Dictionary)
a = input()
b = input()

sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) > 0:
        print('NO')
        break
else:
    print('YES')

# Method Lecture(List)
a = input()
b = input()

str1 = [0] * 52 # 대문자26, 소문자26
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1 # 아스키넘버 A = 65
    else:
        str1[ord(x) - 71] += 1 # 아스키넘버 a = 97

for i in range(52):
    if str1[i] != str2[i]:
        print('NO')
        break

else:
    print('YES')
