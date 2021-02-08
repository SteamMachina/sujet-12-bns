def maxi(T):
  max = T[0]
  id = 0
  for i in range(len(T)):
    if max < T[i]:
      max = T[i]
      id = i
  return (max, id)
assert maxi([1,5,6,9,1,2,3,7,9,8]) == (9,3)
