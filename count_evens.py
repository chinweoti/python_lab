
# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  count = 0
  for e in nums:
    if e%2 == 0:
      count += 1
  return count
