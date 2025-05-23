ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]

numb = []
x = 0

for i in range(len(ar2)):
  ar3 = ar2[i]

  for j in range(len(ar3)):
      f = ar3[j]
      numb.append(f)
  for i in range (len(numb)):
     num = numb[i]
     x = num + x
  print(x, ",", end=" ")
