
# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
  if len(nums) >= 1  and (nums[0] ==6 or nums[-1]==6):
    return True
  return False
