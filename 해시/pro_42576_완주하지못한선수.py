def solution(participant, completion):
    participant.sort()
    completion.sort()

    l = len(completion)
    for i in range(l):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[l]

if __name__ =='__main__':
    a, b= ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
    print(solution(a, b))