
# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
# Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
# Given 3 ints, a b c, return the sum of their rounded values.

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
  if num < 10:
    if num < 5:
      return 0
    if num >= 5:
      return 10
  
  if num % 10 < 5:
    return num - (num%10)
  return num + (10 - (num%10))
    
