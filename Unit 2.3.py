print("Factorial Calculator:")
n = input("Enter a value fro the upper limit, n: ")
n = int(n)
i = 0
p = 1
while (i <= n):
  print(i, "! =", p)
  i = i + 1
  p = p * i
