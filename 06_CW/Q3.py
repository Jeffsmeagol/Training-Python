# create a string made of the middle three characters
def midString(stg):
  m =''
  id = len(stg)//2
  m = m + stg[id-1] + stg[id] + stg[id + 1]
  print(m)
midString('jason')