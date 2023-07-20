# get a string made of the first 2 and last 2 char of a given string
import re

str = input('enter string: ')
if len(str) > 1:
  x = re.search(r'^(\w{2})', str)
  y = re.search(r'\w{2}$', str)
  print(x.group(0) + y.group(0))
  
else:
  print('Empty String')