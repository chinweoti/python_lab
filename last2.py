
# Given a string, return the count of the number of times that a substring length 2 appears in the string and
# also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  last2 = str[-2:]
  count = 0
  if len (str) <2:
    return 0
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count += 1
  return count
      
  
