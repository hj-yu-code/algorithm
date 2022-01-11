from collections import deque
def palindrome(word):
    list_word = list(word)
    for i in range(0, len(list_word) // 2):
        if list_word[i] == list_word[len(list_word) - 1 - i]:
            continue
        else:
            return False
    return True
def is_palindrome(word_list):
    if palindrome(word_list[0]+word_list[1]) or palindrome(word_list[1]+word_list[0]):
        return True
    return False
    
def is_all_palindrome(word_list):
    if len(word_list) ==2:
        if is_palindrome(word_list):
            return True
        else:
            return False
    
    check = word_list[0]
    word_list = word_list[1:]
    for word in word_list:
        if is_palindrome([check, word]):
            word_list = word_list.remove(word)
            return is_all_palindrome(word_list)
    return False

def solution(P):
    ans= []
    
    first = P[0]
    P = P[1:]
    print(P)

    for check in P:
        check_list = P[:]
        check_list.remove(check)
        print('check: ', check_list)
        if is_palindrome([first, check]) and is_all_palindrome(check_list):
            print('correct: ', check)
            ans.append(check)
    return ans
if __name__ =='__main__':
    a = ["11","111","11","211"]
    a = ["21","123","111","11"]
    # b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(a))