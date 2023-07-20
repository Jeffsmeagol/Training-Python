import re
'''
count = 0
pattern = re.compile('ab')
matcher = pattern.finditer('abaababa')
for match in matcher:
  count += 1
  print(match.start(),'...',match.end(),'....', match.group())
  print('The number of occurrences: ', count)

matcher = re.finditer('[abc]', 'a7b@k9Z')
for match in matcher:
  print(match.start(), '........', match.group())

matcher = re.finditer('a?', 'abaabaaab')
for match in matcher:
  print(match.start(), '........', match.group())

s = input('Enter pattern to check: ')
m = re.match(s, 'abcabdefg')
if m != None:
  print('Match is available')
  print('start index:', m.start(), 'and End Index:', m.end())
else:
  print('Match is not available')

s = input('Enter pattern to check: ')
m = re.fullmatch(s, 'ababab')
if m != None:
  print('Match is available')
  print('start index:', m.start(), 'and End Index:', m.end())
else:
  print('Match is not available')

s = input('Enter pattern to check: ')
m = re.search(s, 'abaaaba')
if m != None:
  print('Match is available')
  print('start index:', m.start(), 'and End Index:', m.end())
else:
  print('Match is not available')

l = re.findall('[0-9]', 'a7b9c5kz')
print(l)

s = re.sub('[a-z]','#', 'a7b9c5kz')
print(s)

s = re.subn('[a-z]','#', 'a7b9c5k8z')
print(s)

l = re.split(',', 'KGF,BB1,BB2')
print(l)
for t in l:
  print(t)

l = re.split('B', 'KGF,BB1,BB2')
print(l)
for t in l:
  print(t)

s = input('Enter Mail id: ')
m = re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com', s)
if m != None:
  print('Valid Mail Id')
else:
  print('Invalid Mail id')
'''
s = input('Enter pattern to check: ')
m = re.match(s, 'abcabdefg')
if m != None:
  print('Match is available')
  print('start index:', m.start(), 'and End Index:', m.end(), m.group())
else:
  print('Match is not available')