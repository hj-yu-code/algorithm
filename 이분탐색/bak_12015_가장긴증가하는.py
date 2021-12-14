#### 아직못품
def uplist(nums):
    L = len(nums)
    
    if L == 2:
        if nums[0] < nums[1]:
            return 1
        return 0
    
    half_L = (L + 1) // 2
    left = uplist(nums[:half_L])
    right = uplist(nums[half_L-1:])

    return left + right


n = input()
A = list(map(int, input().split()))
result = uplist(A)
if result:
    print(result+1)
else:
    print(0)