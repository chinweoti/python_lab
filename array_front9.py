
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  for e in range(end):
    if nums[e] == 9:
      return True
  return False
