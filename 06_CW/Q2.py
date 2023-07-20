# remove all occurrences of a specific item from a list
list1 = [5, 20, 15, 20, 25, 50, 20]
remList = []
for x in list1:
  if (x not in remList):
    remList.append(x)
print(remList)