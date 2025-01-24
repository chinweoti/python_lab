
# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 

def near_ten(num):
  if num % 10 <= 2 or num % 10 >= 8:
    return True 
  return False
