def unique_list(l):
  newlist = []
  for a in l:
    if a not in newlist:
      newlist.append(a)
  return newlist

print(unique_list([1,2,3,3,3,3,4,5])) 