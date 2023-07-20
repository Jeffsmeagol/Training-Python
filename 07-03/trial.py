from functools import *
'''def decimalConvert(d, number):
  convertedNum = ''
  dividend = number
  while (dividend > 0):
    rem = dividend%d
    match rem:
      case 10:
        rem = 'A'
      case 11:
        rem = 'B'
      case 12:
        rem = 'C'
      case 13:
        rem = 'D'
      case 14:
        rem = 'E'
      case 15:
        rem = 'F'
      case _:
        rem = rem
    convertedNum += str(rem)
    dividend = dividend//d
  return convertedNum[::-1]

print(decimalConvert(8, 13))
for i in range(1, 6):
  octNum = decimalConvert(4, i)
  print(octNum)

def total_count(dit):
    return reduce(lambda x, y: x + y, [v for v in dit.values()])

def minion_game(string):
  # your code goes here
  VOWELS = 'AEIOU'
  match_dict_k = {}
  match_dict_s = {}
  for i in range(len(string)):
    j = 1
    while (j <= (len(string) - i)):
      m_k = string[i:(i+j)]
      print(m_k)
      if m_k[0] in VOWELS:
        if m_k in match_dict_k:
          match_dict_k[m_k] += 1
        else:
          match_dict_k[m_k] = 1
      else:
        if m_k in match_dict_s:
          match_dict_s[m_k] += 1
        else:
          match_dict_s[m_k] = 1
      j += 1
  print(match_dict_k, match_dict_s)
  
  ktc = total_count(match_dict_k)
  stc = total_count(match_dict_s)
  print(ktc)
  print(stc)
  if ktc > stc:
    print('KELVIN', ktc)
  elif ktc < stc:
    print('STUART', stc)
  else:
    print('DRAW')
print(minion_game('BANANA'))

print(max(False, -2))
def func1():
    try:
        return 1
    finally:
        return 2
print(func1())
'''
print(4+3%5)