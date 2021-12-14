# https://www.acmicpc.net/problem/1439

text = input()
first = text[0]
count = 1

for i in text:
    if first != i:
        first = i
        count+= 1

print(count // 2)
