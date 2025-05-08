a = -5
def fun(a: int):
  if a < 0:
     a = a - a - a
  return a

print(fun(a))
