
# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  emp_str = ""
  for i in range(len(str)):
    emp_str += str[i]*2
  return emp_str
