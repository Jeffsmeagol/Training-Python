class Demo:
  def __init__(self):
    print('No-Arg Constructor')
  def __init__(self, a):
    print('One-Arg constructor')
  def __init__(self, a=0, b=0):
    print('Two-Arg Constructor')
# d1 = Demo()
d1 = Demo(10)
d1 = Demo(10, 20)
