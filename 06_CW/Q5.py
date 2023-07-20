# find the largest item from a given list using list comprehension
x = [4, 6, 8, 24, 12, 2]

from functools import reduce
y = reduce(lambda a, b : a if a > b else b, x)
print(y)

# m = x[0]
# for i in x:
#   if i > m:
#     m = i
# print(m)