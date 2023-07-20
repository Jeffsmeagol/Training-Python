'''
class Book:
  def __init__(self, pages):
    self.pages = pages
  def __add__(self, others):
    return self.pages + others.pages
b1 = Book(100)
b2 = Book(200)
print(b1 + b2)
'''
class Student:
  def __init__(self, name, rollno):
    self.name = name
    self.rollno = rollno
  def __str__(self):
    return 'This is Student object with name {} and roll no {}'.format(self.name, self.rollno)
s1 = Student('Ram', 10)
s2 = Student('Rahim', 12)
print(s1)
print(s2)