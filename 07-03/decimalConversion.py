def print_formatted(number):
  # your code goes here
  def decimalConvert(d, num):
    convertedNum = ''
    dividend = num
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
  
  wide = len(decimalConvert(2, number))
  result = ''
  for i in range(1, number+1):
    octNum = decimalConvert(8, i)
    hexNum = decimalConvert(16, i)
    binNum = decimalConvert(2, i)
    result += str(i).rjust(wide) + ' ' + octNum.rjust(wide) + ' ' + hexNum.rjust(wide) + ' ' + binNum.rjust(wide) + '\n'
  return result

print(print_formatted(17))