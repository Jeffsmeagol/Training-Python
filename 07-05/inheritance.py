'''
class One:
  def m1(self):
    print('Parent class m1 method')
class Two(One):
  def m2(self):
    print('Child class m2 method')
c = Two()
c.m1()
c.m2()

class A:
  def m1(self):
    print('Parent class A: m1 Method')
class B(A):
  def m2(self):
    print('Child class B deived from A: m2 Method')
class C(B):
  def m3(self):
    print('Child class C derived from B: m3 Method')
obj = C()
obj.m1()

class P1:
  def m1(self):
    print('Parent1 Method')
class P2:
  def m1(self):
    print('Parent2 Method')
class C(P2, P1):
  def m2(self):
    print('Child Method')
c = C()
c.m1()
c.m2()

class A:
  def __init__(self):
    print('super class A constructor')
class B(A):
  def m1():
    print()
'''
class Number:
  def __init__(self, num):
    self.num = num
  def display(self):
    print(self.num)
class Power(Number):
  def __init__(self, num, n):
    super().__init__(num)
    self.n = n
  def display(self):
    super().display()
    print(self.n)
p = Power(2, 3)
p.display()