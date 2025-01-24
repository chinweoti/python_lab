# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
# So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  for i in range(len(str)-2):
    if str[i-1] != '.' and str[i] =='x' and str[i+1] == 'y' and str[i+2] == 'z':
      return True
  return False
