"""
Return Missing Balanced Numbers
A balanced array would be an array in which each element appears the same number of times.
Given an array with n elements, return a dictionary with the key as the element and the value as the count of elements needed to balance the given array.
Signature 
HashMap<Object, Integer> returnMissingBalancedNumbers(Object[] elements)
Input 
Array of mixed elements (integers, strings, etc.)
Output
Object with a mixed key, and an integer value
Examples
elements: ["a", "b", "abc", "c", "a"]
output: {"b":1, "abc":1, "c":1}

elements: [1,3,4,2,1,4,1]
output: {2:2, 3:2, 4:1}

elements: [4,5,11,5,6,11]
output: {4:1,6:1}
"""

def return_missing_balanced_numbers(input):
  # Write your code here
  
  result = {}
  res = {}
  max = 0
  for e in input:
    result[e] = result.get(e,0)+1
 
  for key, value in result.items():
    if value > max:
      max = value
  for key, value in result.items():
    if value < max:
      res[key] = max-value
  return res
      