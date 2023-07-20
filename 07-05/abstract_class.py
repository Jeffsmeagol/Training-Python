
from abc import *

'''
class Demo:
  @abstractmethod
  def one(self):
    pass
  def two(self):
    print('This is an implemented mehod')
'''
class Demo1(ABC):
  @abstractmethod
  def m1(self):
    pass
  @abstractmethod
  def m2(self):
    pass
  def m3(self):
    print('implemented method')
d = Demo1()
d.m3()