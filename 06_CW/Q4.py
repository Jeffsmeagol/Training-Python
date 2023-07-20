# write a program to create a recursive function to calculate the sum of numbers from 0 to 10
def sumNums(x, y):
  if (x > y):
    return 0
  else:
    return x + sumNums(x+1, y)
print(sumNums(0, 10))