
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  abs_diff = abs(n-21)
  if n > 21:
    return abs_diff*2
  else:
    return abs_diff