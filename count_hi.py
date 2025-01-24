
# Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  target = 'hi'
  count = 0
  for i in range(len(str)-1):
    if str[i] + str[i+1] == target:
      count += 1
  return count