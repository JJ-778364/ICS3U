n = input("Give me a value of n: ")
n = int(n)
j = 0
t = 0
f = 0
p = 1
print("Counting from j = 1 to", n, ":")
print("    j      tri         factorial")
while j<n:
  j = j + 1
  j = int(j)
  t = j * (j + 1)
  t = t/2
  t = int(t)
  f = f + 1
  p = p * f
  p = int(p)
  print("     ", j, "    ", t, "         ", p)
