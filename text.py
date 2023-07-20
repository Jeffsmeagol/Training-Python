# print('ap' in 'apple')
course = 'Python programming language, Python is easy'
# print(course.find('p'))
# print(course.find('a', 21))
# print(course.index('Python'))
# print(course.count('P'))
course2 = course.replace('Python', 'java')
# print(course2)
# print(course)
# print(id(course))
# print(id(course2))
# y = 4
# x = y = 2
# y = 3
# print(id(x))
# print(id(y))
# print(x)
# def removeOddValue(pString):
#     oString = ''
#     for x in pString:
#         if((pString.index(x) % 2) == 1):
#             oString = oString + x
#     return oString

# print(removeOddValue('sddjdskio'))
'''
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))
if (a > b):
    if(a > c):
        print(str(a) + ' is the greatest')
    else:
        print(str(c) + ' is the greatest')
else:
    if(b > c):
        print(str(b) + ' is the greatest')
    else:
        print(str(c) + ' is the greatest')



def myFunc(sting):
    x = 1
    while(x < len(sting)):
        print(sting[x])
        x+=2
mySt = input('enter your string')
myFunc(mySt)


def reverseString(sting):
    rStng = ''
    x = len(sting) -1
    while(x >= 0):
        rStng = rStng + sting[x]
        x -= 1
    print(rStng)
mySt = input('enter your string')
print(reverseString(mySt))

y = int(input('enter base '))
n = int(input('enter power '))
total = 1
for i in range(1, n+1):
    total = total * y
print(total)


bin = input('enter your binary number ')
c = 0
d = 0
for i in range(len(bin) - 1, -1, -1):
    d = 2**c + int(bin[i])
    c += 1
print(d)


rows = range(1,5)
for x in rows:
    for star in range(1, x+1):
        print('* ', end='')
    print()
    

# myWord = input('enter your word ')
# w = ''
# for x in myWord:
#     c = myWord.count(x)
#     if (c > 1) and (x not in w):
#         w = w + x + str(c) + '   '
# print(w)


# def vowels(word):
#     c = 0
#     for i in word:
#         if (i in 'aeiou'):
#             c += 1
#     return c

# print(vowels('pythonoe'))

def myFact(n):
    total = 1
    for x in range(1, n+1):
        total = total * x
    return total

# myNum = int(input('enter your factorial '))
# print(myFact(myNum))

def display(a, b):
    if (a > b):
        c = a
        a = b
        b = c
    for x in range(a, b+1):
        print('the factorial of {} is {}'.format(x, myFact(x)))

a = int(input('enter the start number: '))
b = int(input('enter the end number: '))
display(a, b)


def sumOfNum(sm):
    s = 0
    for x in str(sm):
        s += int(x)
    return s

def productOfNum(pm):
    p = 1
    for x in str(pm):
        p *= int(x)
    return p

def spyNums(a, b):
    for x in range(a, b+1):
        if (x < 10):
            continue
        if (sumOfNum(x) == productOfNum(x)):
            print(x)

# spyNums(1, 1000)
jup = productOfNum
print(spyNums)
print(type(course))
print(type(jup))

def cart(item, price=20):
    print(item, 'cost is', price)

cart('wert')

def total(x, *y):
    sum = 0
    for i in y:
        sum += i
    print(x + sum)

total()

# def m1(**x):
#     for k, v in x.items():
#         print(k, '=', v)

# m1(a=10, b=20, c=30)
# m1(a=100, name='subbalaxmi')

a = 1
def m1():
    global a
    a = 2
    print(a)
def m2():
    print(a)
m1()
m2()

a = 1
def m():
    a =2
    print(2)
    print(globals()['a'])
m()

def fact(n, y):
    if y == 0:
        return 1
    return n * fact(n, y-1)
    
print(fact(4, 4))

r = range(0, 10)
l = list(r)
print(l)
l[0] = 23
print(l)
print(type(l))
print(type(len))


def tot(**x):
    print(x)
    pass

tot()

a = [1, 2, 3]
b = [3, 0]
c = 'Balu'
d = 'abl'
g = 9
k = g
# a.extend(c)
print(c < d)
print(id(k), id(g))

x = lambda a, b : print(a * b)
x(4, 8)

# items_cost = [999, 888, 1100, 1200, 1300, 777]
# gt_thousand = filter(lambda x: x > 1000, items_cost)
# x = list(gt_thousand)
# print('eligible for discount', x)
# contain_1 = filter(lambda x : '1' in str(x), items_cost)
# print(type(contain_1))
from functools import reduce
gst_cost = [100, 200, 300]
w_gst_cost = reduce(lambda x, y : x + y, gst_cost)
print(w_gst_cost)

s = range(1, 20, 3)
for i in s:
    print(i)
n = [x for x in s if x%2 ==0]
print(n)


a = ['Mike', 'Jack', 'Mohan', 'Kelly']
l = [x for x in a if 'k' in x or 'K' in x]
print(l)

from functools import reduce
a = [123, 772, 333, 111]
b = [reduce(lambda x, y: int(x) + int(y), str(i)) for i in a ]
print(b)

emp_ids = [10, 20, 30, 10, 20, 40, 50, 70]
# print(emp_ids[:5])
print(sorted(emp_ids, reverse=True))
a, b, c, d, e, f, g, h = emp_ids
print(g)

# writ a prog which enters 5 names in a list, sort the list base on the list length

t = (x**2 for x in range(1,6))
print(type(t))
for x in t:
    print(x)

d = {}
n = int(input('enter no of emp: '))
i = 1
while i <= n:
    name = input('enter emp name: ')
    salary = input('enter emp salary: ')
    d[name] = salary
    i += 1
print(d)

d = dict(['56', 'qw', 'se', '98'])

print(d.popitem())
dic = {
    1 : 'ramesh',
    'ty' : 'buy',
    3 : 78,
    'we' : ['po'],
    900 : None
}
for x, y in dic.items():
    print(x, y)
print(dic)

squares = {a: a*a for a in range(1,6)}
print(squares)

#  write a prog which enters a string and using dictionary comprehension, store the letter as a key and the count the value
theStr = input('enter a string: ')
strDict = {s : theStr.count(s) for s in theStr}
print(strDict)

# def removeOddValue(pString):
#     oString = ''
#     for x in pString:
#         if((pString.index(x) % 2) == 1):
#             oString = oString + x
#     return oString

theList = input('enter a string: ').split()
remList = [''.join([s for s in l if ((l.index(s) % 2) == 1)]) for l in theList]
print(remList)
'''
class_Dict = {}
def createClassDict():
    while True:
        print("Enter 'end' to stop")
        roll_no = input("Enter roll number: ")
        if roll_no == "end":
            break
        student_name = input("Enter student name: ")
        class_Dict[roll_no] = student_name
        

def displayClassDict():
    for k, v in class_Dict.items():
        print(k, v)

def addNewPair():
    roll_no = input("Enter new roll number: ")
    student_name = input("Enter new student name: ")
    class_Dict[roll_no] = student_name
    print(class_Dict)

def deleteStudentRecord():
    roll_no = input("Enter roll number of student to be deleted: ")
    class_Dict.pop(roll_no)

def modifyStudentName():
    roll_no = input("Enter roll number of student to be modify: ")
    new_student_name = input("Enter new student name: ")
    class_Dict[roll_no] = new_student_name

createClassDict()
displayClassDict()
addNewPair()
deleteStudentRecord()
modifyStudentName()

class CheckValidity:
    def __init__(self, longString):
        self.longString = longString
    
    def main(self):
        openBrackets = "([{"
        closeBrackets = ")]}"
        check = []
        for s in self.longString:
            if s in openBrackets:
                check.append(s)
            elif s in closeBrackets:
                last = check.pop()
                if openBrackets.index(last) != closeBrackets.index(s):
                    return False