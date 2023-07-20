# count the no of char in a string
theStr = input('enter a string: ')
strDict = {s : theStr.count(s) for s in theStr}
print(strDict)