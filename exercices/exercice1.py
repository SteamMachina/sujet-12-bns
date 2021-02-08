def maxi(T):
  max = T[0]
  id = 0
  for i in range(len(T)):
    if max < T[i]:
      max = T[i]
      id = i
  return (max, id)
