import re
'''
import re
for _ in range(int(input())):
  s = input()
  if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
    print("Valid")
  else:
    print("Invalid")

cc = input('your credit card number: ')
x = re.search(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", cc)
y = re.search(r'([\d])\1\1\1+', cc.replace('-', ''))
if x and not y:
  print('yep')
else:
  print('no')

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.groups(2))
else:
  print("pattern not found")

P = '223232567'
print(re.findall(r'(?=(\d)\d\1)',P))
'''
  
m = re.findall(r'((?<=\w)\W+)\w+\b', 'sp-e!a-&egm-eg!%-')
print(m)
print(re.sub(r'(?<=\w)\W+(?=\w+)', ' ', 'sp-e!a-egm-eg!%-'))
