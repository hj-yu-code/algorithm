#### 아직못품

def solution(s):
    answer = 0

    l = (len(s) // 2) + 1
    for n in range(1, l):
        new_s = ''

        for ptr in range(len(s)):
            if s[ptr:ptr+n] == s[ptr+n:ptr+(2*n)]:
                new_s = 'str'

        

        result = len(new_s)
        answer = min(answer, result)
    
    return answer

if __name__ == '__main__':
    s = "aabbaccc"
    print(solution(s))
        
