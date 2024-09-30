numbers = [3,6,2,8,1]
def iter_total(nums):
    n = 0
    for i in range(0,len(nums)):
        n = n + nums[i]
    #next i 
    return  n
#endfunction

tot = iter_total(numbers)
print(tot)