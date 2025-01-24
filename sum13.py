
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
# so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  sum_nums = 0
  target = 0
  if len(nums) < 1:
    return 0
    
  for i in range(len(nums)):
    if  nums[i] == 13:
      if i + 1 < len(nums):
        nums[i+1] = 0
    else:
      sum_nums += nums[i]
  return sum_nums
    
    
