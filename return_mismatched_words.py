"""

Return Mismatched Words
Given an input of two strings consisting of english letters (a-z; A-Z) and spaces, complete a function that returns a list containing all the mismatched words (case sensitive) between them.
You can assume that a word is a group of characters delimited by spaces.
A mismatched word is a word that is only in one string but not the other.
Add mismatched words from the first string before you add mismatched words from the second string in the output array.
Signature 
static String[] returnMismatched(String str1, String str2)
Input
str1: a string
str2: a string
Note: You can only expect valid english letters (a-z; A-Z) and spaces.
Output
An array containing all words that do not match between str1 and str2.
Examples
str1: "Firstly this is the first string"
str2: "Next is the second string"
output: ["Firstly", "this", "first", "Next", "second"]

str1: ""
str2: ""
output: []

str1: ""
str2: "This is the second string"
output: ["This","is","the","second","string"]

str1: "This is the first string" 
str2: "This is the second string" 
output: ["first", "second"]

str1: "This is the first string extra" 
str2: "This is the second string" 
output: ["first", "extra", "second"]

str1: "This is the first text" 
str2: "This is the second string" 
output: ["first", "text", "second", "string"]
"""



def return_mismatched_words(str1, str2):
  emp_dict = {}
  result = []
  
  if str1 == str2:
    return []
  
  str1 = str1.split()
  str2 = str2.split()
  
  for e in str1:
    emp_dict[e] = emp_dict.get(e, 0) + 1
  for e in str2:
    emp_dict[e] = emp_dict.get(e, 0) + 1
  for key, value in emp_dict.items():
    if value == 1:
      result.append(key)
  return result