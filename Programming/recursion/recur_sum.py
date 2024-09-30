numbers = [3,6,2,8,1]
def recur_total(nums):
    if len(nums)==0:
        return 0
    else:
        return nums[0] + recur_total(nums[1:])
    #endif
#end function

print(recur_total(numbers))