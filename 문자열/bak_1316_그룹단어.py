n = int(input())
count = 0

for _ in range(n):
    word = input()
    now = word[0]
    word_list = [now]
    
    nop = 0
    
    for i in word:
        if i != now:
            if i in word_list:
                nop = 1
                break
            word_list.append(i)
            now = i

    if not nop:
        count +=1
print(count)

            