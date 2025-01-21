
# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
  if len(str) % 2 == 0:
    return str[:len(str)/2]
