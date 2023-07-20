# concatenate two lists index-wise
list1 = ['M', 'na', 'i', 'Ke']
list2 = ['y', 'me', 's', 'lly']

concList = []
for x in list1:
  a = x + list2[list1.index(x)]
  concList.append(a)
print(concList)