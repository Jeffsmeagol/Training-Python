'''s = set(range(5))
# print(s)
s1 = set([1.0, 1, 2, 3, 3, 1.0, 2.0])
print(s1)
s2 = set([])
print(s2)
print(type(s2))

s = {10,20,30}
s.add(40)
print(s)
l = [40, 50, 60, 10]
s.update(l, range(5))
s.remove(3)
s.pop()
s.discard(50)
print(s)

a = 10
b = 12
c = a|b   #bitwise operator
d = a&b
print(c, d)

x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
# print(x|y)
# print(x.union(y))
# print(y.intersection(x))
# print(x&y)
print(x.difference(y))
print(x-y)
print(y-x)
print(x.symmetric_difference(y))
print(x^y)
'''
vowels = {'a', 'e', 'i', 'o', 'u'}
fSet = frozenset(vowels)
print(type(fSet))