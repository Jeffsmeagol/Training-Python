'''
class Demo:
  def m1(self):
    print('no-arg method')
  def m1(self, a):
    print('one-arg method')
  def m1(self, a, b):
    print('two-arg method')
d = Demo()
d.m1()
# d.m1(10)
# d.m1(10, 20)
'''
class Demo:
  def sum(self, a=None, b=None, c=None):
    if a != None and b != None and c != None:
      print('The Sum of 3 Numbers', a + b + c)
    elif a != None and b != None:
      print('The Sum of 2 Numbers', a + b)
    else:
      print('Please provide 2 or 3 arguments')
d = Demo()
d.sum(10,20,30)
d.sum(10,20)
d.sum(10)