#### 아직못품
def solution(food_times, k):
    
    if sum(food_times)<= k:
        return -1
    
    answer = 0
    l = len(food_times)-1
    ptr = 0
    
    for time in range(k):
        food_times[ptr] -= 1
    
        ptr +=1
        if ptr > l:
            ptr = 0

        while food_times[ptr]==0:
            ptr +=1
            if ptr > l:
                ptr = 0

        print(food_times, ptr)
    
    while food_times[ptr]==0:
        ptr +=1
        if ptr > l:
            ptr = 0
            
    return ptr+1

if __name__ == '__main__':
    food_times = [3, 1, 2]
    k = 5
    print(solution(food_times, k))