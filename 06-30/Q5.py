# 
firstStr = input('enter first string: ')
secondStr = input('enter second string: ')
pfirstStr = firstStr.replace(firstStr[:2], secondStr[:2])
psecondStr = secondStr.replace(secondStr[:2], firstStr[:2])
print(pfirstStr + ' ' + psecondStr)