'''
def hello_decorator(func):
  def inner1():
    print('Hello, this is before function execute')
    func()
    print('This is after function execution')
  return inner1

def function_to_be_used():
  print('This is inside the function !!')

function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()
'''
import time
import math

def calculate_time(func):
  def inner1(*args, **kwargs):
    begin = time.time()
    func(*args, **kwargs)
    end = time.time()
    print('Total time taken in: ', func.__name__,end-begin)
  return inner1

@calculate_time
def factorial(num):
  time.sleep(2)
  print(math.factorial(num))

factorial(10)