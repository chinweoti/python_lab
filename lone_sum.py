
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, 
# it does not count towards the sum.

def lone_sum(a, b, c):
  if a == b and b == c:
    return 0
  if a != b and a==c:
    return b
  if b == c and b!= a:
    return a
  if c != a and a == b:
    return c
  return a+b+c