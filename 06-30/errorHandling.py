'''print('One')
print('Two')
try:
  print(10/0)
except ZeroDivisionError:
  print()
print('Four')
print('Five')

try:
  print(10/0)
except ZeroDivisionError as z:
  print(z)

try:
  x = int(input('Enter First Number: '))
  y = int(input('Enter Second Number: '))
  print(x/y)
except ZeroDivisionError:
  print('Can\'t Divide with Zero')
except ValueError:
  print('please provide int value only')

try:
  x = int(input('Enter First Number: '))
  y = int(input('Enter Second Number: '))
  print(x/y)
except (ZeroDivisionError, ValueError) as e:
  print('Please Provide valid numbers only and problem is: ', e)

try:
  x = int(input('Enter First Number: '))
  y = int(input('Enter Second Number: '))
  print(x/y)
except ZeroDivisionError:
  print('ZeroDivisionError: Can\'t Divide with Zero')
except:
  print('Default Except: Please provide valid input only')

try:
  print('try block')
  print(10/0)
except ZeroDivisionError:
  print('except block')
finally:
  print('finally block')

try:
  print('try block')
  print(10/0)
except NameError:
  print('except block')
finally:
  print('finally block')

try:
  print('Outer try block')
  
  try:
    print('inner try block')
    print(10/0)
  except ZeroDivisionError:
    print('inner except block')
  finally:
    print('inner finally block')
except NameError:
  print('outer except block')
finally:
  print('outer finally block')

try:
  print('try block')
except:
  print('except: Handling code')
else:
  print('else block')
finally:
  print('finally block')
'''
# generating custom exception in python
try:
  x = int(input('Enter a number between positive integer: '))
  if x < 0:
    raise ValueError(x)
except ValueError as e:
  print('You provided {}. Please provide positive integer values only'.format(e))
