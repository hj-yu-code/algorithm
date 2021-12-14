def binary_search (arr, val):
    first, last = 0, len(arr)-1
    while first <= last :
        mid = (first + last) // 2
        if arr[mid] == val: return 1
        if arr[mid] > val: last = mid - 1
        else: first = mid + 1
    return 0


n = int(input())
A_list = list(map(int, input().split()))
A_list.sort()
n = int(input())
find_list = list(map(int, input().split()))

for val in find_list:
    mid = binary_search(A_list, val)
    print(mid)


####다른방법
# # 첫번째 인풋 개수 N
# N = int(input())
# # N개의 자연수 input 리스트
# N_list = set(input().split(' '))

# # 두번째 인풋 개수 M
# M = int(input())
# # M개의 자연수 input 리스트
# M_list = input().split(' ')

# for i in M_list:
#     if i in N_list: print(1)
#     else: print(0)

##### 갯수까지 구하기
# def binary_search (arr, val):
#     first, last = 0, len(arr)-1
#     while first <= last :
#         mid = (first + last) // 2
#         if arr[mid] == val: return mid
#         if arr[mid] > val: last = mid - 1
#         else: first = mid + 1
#     return -1

# def count_num(arr, mid):
#     first, last = mid, mid
#     while first >=0 :
#         if arr[first] != arr[mid]:
#             break
#         first -= 1
    
#     while last < len(arr) :
#         if arr[last] != arr[mid]:
#             break
#         last += 1
#     return last - first - 1

# n = int(input())
# A_list = list(map(int, input().split()))
# A_list.sort()
# n = int(input())
# find_list = list(map(int, input().split()))

# for val in find_list:
#     mid = binary_search(A_list, val)
#     if mid == -1:
#         print(0)
#     else:
#         count = count_num(A_list, mid)
#         print(count)