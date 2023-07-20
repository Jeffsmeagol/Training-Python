import re
f1 = open('07-04/inputTry.txt', 'r')
f2 = open('07-04/outputTry.txt', 'w')
for line in f1:
  items = re.findall('[7-9]\d{9}', line)
  for n in items:
    f2.write(n+'\n')
print('Extracted all Mobile Numbers into output.txt')