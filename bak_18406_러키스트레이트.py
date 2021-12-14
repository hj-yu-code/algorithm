nums = list(map(int, input()))

ln = int(len(nums)/2)

r = sum(nums[:ln])
l = sum(nums[ln:])

if r == l:
    print("LUCKY")

else :
    print("READY")