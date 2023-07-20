'''
class Employee:
  def display(self):
    print('Hello my name is Rahul')

emp_obj1 = Employee()
emp_obj1.display()

emp_obj2 = Employee()
emp_obj2.display()

class Employee:
  def __init__(self):
    print('message from constructor')

emp = Employee()
emp.__init__()

print(dir(Employee))

class Employee:
  def __init__(self, id):
    self.id = id
    print('Employee id is: ', self.id)

e1 = Employee(1)
e2 = Employee(2)

class Employee:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    print('Employee id is: ', self.id)
  
  def display(self):
    print('Hello my id is :', self.id)
    print('My name is:', self.name)

e1 = Employee(1, 'Nithin')
e1.display()
e2 = Employee(2, 'Arjun')
e2.display()

class Student:
  def __init__(self, name, id):
    self.name = name
    self.id = id

s1 = Student('Nitya', 1)
s2 = Student('Anushka', 2)
print('Student1 info:')
print('Name:', s1.name)
print('id:', s1.id)
print('Student2 info:')
print('Name:', s2.name)
print('id:', s2.id)

class Student:
  def __init__(self, name, id):
    self.__name = name
    self.__id = id

s1 = Student('Nitya', 1)
s2 = Student('Anushka', 2)
print('Student1 info:')
print('Name:', s1.__name)
print('id:', s1.__id)
print('Student2 info:')
print('Name:', s2.__name)
print('id:', s2.__id)

class Employee:
  def __init__(self):
    self.eno = 1
    self.ename = 'Nithya'
    self.esal = 100

e = Employee()
print(e.__dict__)

class Student:
  def m1(self):
    self.a = 11
    self.b = 21
    self.c = 34
    print(self.a)
    print(self.b)
    print(self.c)
s = Student()
# s.m1()
print(s.__dict__)

class Test:
  def __init__(self):
    print('This is constructor')
  def m1(self):
    print('This is instance method')

t = Test()
t.m1()
t.a = 10
t.b = 20
t.c = 55
print(t.a)
print(t.b)
print(t.c)
print(t.__dict__)

class Demo:
  def m1(self):
    Demo.b = 20
obj = Demo()
obj.m1()
print(Demo.__dict__)
print(Demo.b)

class Demo:
  def m(self):
    a = 10
    print(a)
  def n(self):
    print(a)
d = Demo()
d.n()

class Demo:
  def __init__(self, a):
    self.a = a
  def m(self):
    print(self.a)
d = Demo(10)
d.m()

class Customer:
  def set_name(self, name):
    self.name = name
  def set_id(self, id):
    self.id = id
c = Customer()
c.set_name('Balayya')
c.set_id(1)
print(c.name)

class Customer:
  def set_name(self, name):
    self.name = name
  def set_id(self, id):
    self.id = id
  def get_name(self):
    return self.name
  def get_id(self):
    return self.id
c = Customer()
c.set_name('Balayya')
c.set_id(1)
print('My name is: ', c.get_name())
print('My id is: ', c.get_id())

class Pizza:
  radius = 200
  @classmethod
  def get_radius(cls):
    return cls.radius
print(Pizza.get_radius())

class Demo:
  @staticmethod
  def sum(x, y):
    print(x + y)
  @staticmethod
  def multiply(x, y):
    print(x*y)
Demo.sum(2, 3)
Demo.multiply(2,4)
'''
class A:
  def __init__(self):
    print('outer class object creation')
  class B:
    def __init__(self):
      print('inner class object creation')
    def m1(self):
      print('inner class method')
a = A()
b = a.B()
b.m1()