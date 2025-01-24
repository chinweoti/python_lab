
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.

def big_diff(nums):
  big = max(nums)
  small = min(nums)
  if len(nums) < 2:
    return 0
  return (big - small)
  
  